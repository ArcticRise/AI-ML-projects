"""
# Deep Q-Learning for Lunar Landing

This program utlizes PyTourch and gynmasium to implement a Deep Q Learning algorithm
to implement the Lunar Landing problem.

reference to lunar landing: https://gymnasium.farama.org/environments/box2d/lunar_lander/


"""

import os
import random
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.autograd as autograd
from torch.autograd import Variable
from collections import deque, namedtuple
import glob
import io
import base64
import imageio
from IPython.display import HTML, display
from gym.wrappers.monitoring.video_recorder import VideoRecorder
import gymnasium as gym

"""## Part 1 - Building the AI

### Creating the architecture of the Neural Network
"""

class NeuralNetwork(nn.Module):

  def __init__(self, state_size, action_size, seed=42) -> None:
      super(NeuralNetwork, self).__init__()
      self.seed = torch.manual_seed(seed)
      self.fc1 = nn.Linear(state_size, 64) #First Fully Connected Layer of nn
      self.fc2 = nn.Linear(64, 64)
      self.fc3 = nn.Linear(64, action_size)

  def forward(self, state):
      x = self.fc1(state)
      x = F.relu(x)
      x = self.fc2(x)
      x = F.relu(x)
      return self.fc3(x)

"""## Training the AI"""

env = gym.make('LunarLander-v2')
state_shape = env.observation_space.shape
state_size = env.observation_space.shape[0]
number_actions = env.action_space.n
print("State Shape: {}, State_size: {}, Num of Actions: {}".format(state_shape,state_size,number_actions))

"""
### Initialize the hyperparameters
"""

learning_rate = 5e-4
minibatch_size = 100 # Common size for deepq learning (100)
gamma = 0.99 # Note Closer to zero mean dont look at future closer to 1 mean look at and account for future
replay_buffer_size = int(1e5)
tau = 1e-3

"""### Experience Replay"""

class ReplayMemory(object):

  def __init__(self, capacity) -> None:
      self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
      self.capacity = capacity #Max size of Memory buffer
      self.memory = []

  #Add Event, if memory is greater than capacity remove oldest event
  def add_event(self, event):
    self.memory.append(event)
    if len(self.memory) > self.capacity:
      del self.memory[0]

  def sample(self,batch_size):
    experiences = random.sample(self.memory,k=batch_size)
    states = torch.from_numpy(np.vstack([exp[0] for exp in experiences if exp is not None])).float().to(self.device)
    actions = torch.from_numpy(np.vstack([exp[1] for exp in experiences if exp is not None])).long().to(self.device)
    rewards = torch.from_numpy(np.vstack([exp[2] for exp in experiences if exp is not None])).float().to(self.device)
    next_states = torch.from_numpy(np.vstack([exp[3] for exp in experiences if exp is not None])).float().to(self.device)
    dones = torch.from_numpy(np.vstack([exp[4] for exp in experiences if exp is not None]).astype(np.uint8)).float().to(self.device)
    return states, next_states, actions, rewards, dones

"""### DQN class w Epsilon Greedy Strategy"""

class Agent():

  def __init__(self, state_size, action_size):
      self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
      self.state_size = state_size
      self.action_size = action_size
      self.local_qnetwork = NeuralNetwork(state_size,action_size).to(self.device)
      self.target_qnetwork = NeuralNetwork(state_size,action_size).to(self.device)
      self.optimizer = optim.Adam(self.local_qnetwork.parameters(), lr = learning_rate)
      self.replay_memory = ReplayMemory(replay_buffer_size)
      self.t_step = 0

  #Store experiences and learn from them
  def step(self, state, action, reward, next_state, done):
    self.replay_memory.add_event((state, action, reward, next_state, done))
    self.t_step += 1

    if self.t_step % 4 == 0:
      if len(self.replay_memory.memory) > minibatch_size:
        experiences = self.replay_memory.sample(100)
        self.learn(experiences, gamma)

  def act(self, state, epsilon = 0.):
    state = torch.from_numpy(state).float().unsqueeze(0).to(self.device)
    self.local_qnetwork.eval()
    with torch.no_grad():
      action_values = self.local_qnetwork(state)
    self.local_qnetwork.train()

    #Epislon Greedy Selection Process
    if random.random() > epsilon:
      return np.argmax(action_values.cpu().data.numpy())
    else:
      return random.choice(np.arange(self.action_size))

  def learn(self, experiences, gamma):
    states,next_states,actions,rewards,dones = experiences
    next_q_targets = self.target_qnetwork(next_states).detach().max(1)[0].unsqueeze(1)
    q_targets = rewards + (gamma * next_q_targets * (1-dones))
    q_expected = self.local_qnetwork(states).gather(1, actions)
    loss = F.mse_loss(q_expected,q_targets)
    self.optimizer.zero_grad()
    loss.backward() # Back propigate
    self.optimizer.step()
    self.soft_update(self.local_qnetwork, self.target_qnetwork, tau)

  def soft_update(self,local_model,target_model, tau):
    for target_param, local_param in zip(target_model.parameters(),local_model.parameters()):
      target_param.data.copy_(tau * local_param.data + (1.0 - tau) * target_param.data)

"""### Initializing the DQN agent"""

agent = Agent(state_size,number_actions)

"""### Training the DQN agent"""

number_episodes = 1000
maximum_number_t_steps_per_episode = 1000
epsilon_starting_value = 1.0
epsilon_end_value = 0.01
epsilon_decay_value = 0.995
epsilon = epsilon_starting_value
scores_on_100_episodes = deque(maxlen=100)

for episode in range(1,number_episodes+1):
  state, _ = env.reset()
  score = 0
  for t in range(maximum_number_t_steps_per_episode):
    action = agent.act(state, epsilon)
    next_state,reward,done,_,_ = env.step(action)
    agent.step(state,action,reward,next_state,done)
    state = next_state
    score += reward
    if done:
      break
  scores_on_100_episodes.append(score)
  epsilon = max(epsilon_end_value, (epsilon*epsilon_decay_value))
  print('\rEpisode {}\tAverage Score: {:.2f}'.format(episode, np.mean(scores_on_100_episodes)), end="")
  if episode%100 == 0:
    print('\rEpisode {}\tAverage Score: {:.2f}'.format(episode, np.mean(scores_on_100_episodes)))
  if np.mean(scores_on_100_episodes) >= 200.0:
    print('\nEnvironment solved in {:d} episodes! \tAverage Score: {:.2f}'.format(episode, np.mean(scores_on_100_episodes)))
    torch.save(agent.local_qnetwork.state_dict(), 'checkpoint.pth')
    break

"""### Generate Video Of Results!!!"""

def show_video_of_model(agent, env_name):
    env = gym.make(env_name, render_mode='rgb_array')
    state, _ = env.reset()
    done = False
    frames = []
    while not done:
        frame = env.render()
        frames.append(frame)
        action = agent.act(state)
        state, reward, done, _, _ = env.step(action.item())
    env.close()
    imageio.mimsave('video.mp4', frames, fps=30)

show_video_of_model(agent, 'LunarLander-v2')

def show_video():
    mp4list = glob.glob('*.mp4')
    if len(mp4list) > 0:
        mp4 = mp4list[0]
        video = io.open(mp4, 'r+b').read()
        encoded = base64.b64encode(video)
        display(HTML(data='''<video alt="test" autoplay
                loop controls style="height: 400px;">
                <source src="data:video/mp4;base64,{0}" type="video/mp4" />
             </video>'''.format(encoded.decode('ascii'))))
    else:
        print("Could not find video")

show_video()