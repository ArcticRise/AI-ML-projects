import re

dict = {'the': 'DET', 'of': 'ADP', 'to': 'PART', 'and': 'CCONJ', 'a': 'DET', 'in': 'ADP', 'is': 'VERB', 'it': 'PRON', 'you': 'PRON',
 'that': 'DET', 'he': 'PRON', 'was': 'AUX', 'for': 'ADP', 'on': 'ADP', 'are': 'VERB', 'with': 'ADP', 'as': 'ADP', 'I': 'PRON',
 'his': 'PRON', 'they': 'PRON', 'be': 'VERB', 'at': 'ADP', 'one': 'NUM', 'have': 'VERB', 'this': 'DET', 'from': 'ADP',
 'or': 'CCONJ', 'had': 'VERB', 'by': 'ADP', 'hot': 'ADJ', 'but': 'CCONJ', 'some': 'DET', 'what': 'PRON', 'there': 'ADV',
 'we': 'PRON', 'can': 'AUX', 'out': 'ADP', 'other': 'ADJ', 'were': 'AUX', 'all': 'DET', 'your': 'PRON', 'when': 'ADV',
 'up': 'ADP', 'use': 'NOUN', 'word': 'NOUN', 'how': 'ADV', 'said': 'VERB', 'an': 'DET', 'each': 'DET',
 'she': 'PRON', 'which': 'DET', 'do': 'VERB', 'their': 'PRON', 'time': 'NOUN', 'if': 'SCONJ',
 'will': 'AUX', 'way': 'NOUN', 'about': 'ADP', 'many': 'ADJ', 'then': 'ADV', 'them': 'PRON',
 'would': 'AUX', 'write': 'VERB', 'like': 'ADP', 'so': 'ADV', 'these': 'DET', 'her': 'PRON',
 'long': 'ADJ', 'make': 'VERB', 'thing': 'NOUN', 'see': 'VERB', 'him': 'PRON', 'two': 'NUM',
 'has': 'AUX', 'look': 'VERB', 'more': 'ADJ', 'day': 'NOUN', 'could': 'AUX', 'go': 'VERB', 'come': 'VERB',
 'did': 'VERB', 'my': 'PRON', 'sound': 'NOUN', 'no': 'INTJ', 'most': 'ADJ', 'number': 'NOUN', 'who': 'PRON',
 'over': 'ADP', 'know': 'NOUN', 'water': 'NOUN', 'than': 'SCONJ', 'call': 'NOUN', 'first': 'ADJ', 'people': 'NOUN',
 'may': 'AUX', 'down': 'ADP', 'side': 'NOUN', 'been': 'VERB', 'now': 'ADV', 'find': 'VERB', 'any': 'DET', 'new': 'ADJ',
 'work': 'NOUN', 'part': 'NOUN', 'take': 'NOUN', 'get': 'VERB', 'place': 'NOUN', 'made': 'VERB', 'live': 'NOUN',
 'where': 'ADV', 'after': 'ADP', 'back': 'ADP', 'little': 'ADJ', 'only': 'ADV', 'round': 'NOUN', 'man': 'NOUN',
 'year': 'NOUN', 'came': 'VERB', 'show': 'NOUN', 'every': 'DET', 'good': 'ADJ', 'me': 'PRON', 'give': 'VERB', 'our': 'PRON',
 'under': 'ADP', 'name': 'NOUN', 'very': 'ADV', 'through': 'ADP', 'just': 'ADV', 'form': 'NOUN', 'much': 'ADJ', 'great': 'ADJ',
 'think': 'NOUN', 'say': 'VERB', 'help': 'NOUN', 'low': 'ADJ', 'line': 'NOUN', 'before': 'ADP', 'turn': 'NOUN', 'cause': 'NOUN',
 'same': 'ADJ', 'mean': 'NOUN', 'differ': 'VERB', 'move': 'NOUN', 'right': 'NOUN', 'boy': 'NOUN', 'old': 'ADJ', 'too': 'ADV',
 'does': 'AUX', 'tell': 'VERB', 'sentence': 'NOUN', 'set': 'NOUN', 'three': 'NUM', 'want': 'NOUN', 'air': 'NOUN', 'well': 'INTJ',
 'also': 'ADV', 'play': 'NOUN', 'small': 'ADJ', 'end': 'NOUN', 'put': 'NOUN', 'home': 'NOUN', 'read': 'NOUN', 'hand': 'NOUN', 'port':
     'NOUN', 'large': 'ADJ', 'spell': 'NOUN', 'add': 'VERB', 'even': 'ADV', 'land': 'NOUN', 'here': 'ADV', 'must': 'AUX', 'big': 'ADJ',
 'high': 'ADJ', 'such': 'ADJ', 'follow': 'NOUN', 'act': 'NOUN', 'why': 'ADV', 'ask': 'VERB', 'men': 'NOUN', 'change': 'NOUN',
 'went': 'VERB', 'light': 'NOUN', 'kind': 'NOUN', 'off': 'ADP', 'need': 'NOUN', 'house': 'NOUN', 'picture': 'NOUN',
 'try': 'VERB', 'us': 'PRON', 'again': 'ADV', 'animal': 'NOUN', 'point': 'NOUN', 'mother': 'NOUN', 'world': 'NOUN',
 'near': 'SCONJ', 'build': 'NOUN', 'self': 'NOUN', 'earth': 'NOUN', 'father': 'NOUN', 'head': 'NOUN', 'stand': 'NOUN', 'own': 'ADJ',
 'page': 'NOUN', 'should': 'AUX', 'country': 'NOUN', 'found': 'VERB', 'answer': 'NOUN', 'school': 'NOUN', 'grow': 'NOUN', 'study': 'NOUN',
 'still': 'ADV', 'learn': 'VERB', 'plant': 'NOUN', 'cover': 'NOUN', 'food': 'NOUN', 'sun': 'NOUN', 'four': 'NUM', 'thought': 'NOUN', 'let': 'VERB',
 'keep': 'VERB', 'eye': 'NOUN', 'never': 'ADV', 'last': 'ADJ', 'door': 'NOUN', 'between': 'ADP', 'city': 'NOUN', 'tree': 'NOUN', 'cross': 'NOUN',
 'since': 'SCONJ', 'hard': 'ADJ', 'start': 'NOUN', 'might': 'AUX', 'story': 'NOUN', 'saw': 'VERB', 'far': 'ADV', 'sea': 'NOUN', 'draw': 'NOUN',
 'left': 'VERB', 'late': 'ADJ', 'run': 'NOUN', 'donÃ¯Â¿Â½t': 'PROPN', 'while': 'SCONJ', 'press': 'NOUN', 'close': 'ADJ', 'night': 'NOUN', 'real': 'ADJ',
 'life': 'NOUN', 'few': 'ADJ', 'stop': 'VERB', 'open': 'NOUN', 'seem': 'VERB', 'together': 'ADV', 'next': 'ADJ', 'white': 'ADJ', 'children': 'NOUN',
 'begin': 'VERB', 'got': 'VERB', 'walk': 'NOUN', 'example': 'NOUN', 'ease': 'NOUN', 'paper': 'NOUN', 'often': 'ADV', 'always': 'ADV', 'music': 'NOUN',
 'those': 'DET', 'both': 'CCONJ', 'mark': 'NOUN', 'book': 'NOUN', 'letter': 'NOUN', 'until': 'ADP', 'mile': 'NOUN', 'river': 'NOUN', 'car': 'NOUN',
 'feet': 'NOUN', 'care': 'NOUN', 'second': 'NOUN', 'group': 'NOUN', 'carry': 'VERB', 'took': 'VERB', 'rain': 'NOUN', 'eat': 'NOUN', 'room': 'NOUN',
 'friend': 'NOUN', 'began': 'VERB', 'idea': 'NOUN', 'fish': 'NOUN', 'mountain': 'NOUN', 'north': 'NOUN', 'once': 'ADV', 'base': 'NOUN',
 'hear': 'NOUN', 'horse': 'NOUN', 'cut': 'NOUN', 'sure': 'ADJ', 'watch': 'NOUN', 'color': 'NOUN', 'face': 'NOUN', 'wood': 'NOUN', 'main': 'ADJ',
 'enough': 'ADJ', 'plain': 'ADJ', 'girl': 'NOUN', 'usual': 'ADJ', 'young': 'ADJ', 'ready': 'ADJ', 'above': 'ADP', 'ever': 'ADV', 'red': 'ADJ',
 'list': 'NOUN', 'though': 'SCONJ', 'feel': 'VERB', 'talk': 'NOUN', 'bird': 'NOUN', 'soon': 'ADV', 'body': 'NOUN', 'dog': 'NOUN', 'family': 'NOUN',
 'direct': 'ADJ', 'pose': 'NOUN', 'leave': 'VERB', 'song': 'NOUN', 'measure': 'NOUN', 'state': 'NOUN', 'product': 'NOUN', 'black': 'ADJ', 'short': 'ADJ',
 'numeral': 'ADJ', 'class': 'NOUN', 'wind': 'NOUN', 'question': 'NOUN', 'happen': 'VERB', 'complete': 'NOUN', 'ship': 'NOUN', 'area': 'NOUN', 'half': 'ADJ',
 'rock': 'NOUN', 'order': 'NOUN', 'fire': 'NOUN', 'south': 'NOUN', 'problem': 'NOUN', 'piece': 'NOUN', 'told': 'VERB', 'knew': 'VERB', 'pass': 'NOUN',
 'farm': 'NOUN', 'top': 'NOUN', 'whole': 'ADJ', 'king': 'NOUN', 'size': 'NOUN', 'heard': 'VERB', 'best': 'ADJ', 'hour': 'NOUN', 'better': 'ADJ',
 'true': 'ADJ', 'during': 'ADP', 'hundred': 'NUM', 'am': 'VERB', 'remember': 'VERB', 'step': 'NOUN', 'early': 'ADJ', 'hold': 'NOUN', 'west': 'NOUN',
 'ground': 'NOUN', 'interest': 'NOUN', 'reach': 'VERB', 'fast': 'ADJ', 'five': 'NUM', 'sing': 'NOUN', 'listen': 'NOUN', 'six': 'NUM', 'table': 'NOUN',
 'travel': 'NOUN', 'less': 'ADJ', 'morning': 'NOUN', 'ten': 'NUM', 'simple': 'ADJ', 'several': 'ADJ', 'vowel': 'NOUN', 'toward': 'ADP', 'war': 'NOUN',
 'lay': 'VERB', 'against': 'ADP', 'pattern': 'NOUN', 'slow': 'ADJ', 'center': 'NOUN', 'love': 'NOUN', 'person': 'NOUN', 'money': 'NOUN', 'serve': 'VERB',
 'appear': 'VERB', 'road': 'NOUN', 'map': 'NOUN', 'science': 'NOUN', 'rule': 'NOUN', 'govern': 'NOUN', 'pull': 'NOUN', 'cold': 'ADJ', 'notice': 'NOUN',
 'voice': 'NOUN', 'fall': 'NOUN', 'power': 'NOUN', 'town': 'NOUN', 'fine': 'NOUN', 'certain': 'ADJ', 'fly': 'NOUN', 'unit': 'NOUN', 'lead': 'NOUN',
 'cry': 'NOUN', 'dark': 'ADJ', 'machine': 'NOUN', 'note': 'NOUN', 'wait': 'VERB', 'plan': 'NOUN', 'figure': 'NOUN', 'star': 'NOUN',
 'box': 'NOUN', 'noun': 'NOUN', 'field': 'NOUN', 'rest': 'NOUN', 'correct': 'ADJ', 'able': 'ADJ', 'pound': 'NOUN', 'done': 'VERB', 'beauty': 'NOUN',
 'drive': 'NOUN', 'stood': 'VERB', 'contain': 'NOUN', 'front': 'NOUN', 'teach': 'NOUN', 'week': 'NOUN', 'final': 'ADJ', 'gave': 'VERB', 'green': 'NOUN',
 'oh': 'INTJ', 'quick': 'ADJ', 'develop': 'VERB', 'sleep': 'NOUN', 'warm': 'ADJ', 'free': 'ADJ', 'minute': 'NOUN', 'strong': 'ADJ', 'special': 'ADJ', 'mind': 'NOUN', 'behind': 'ADP', 'clear': 'ADJ', 'tail': 'NOUN', 'produce': 'NOUN', 'fact': 'NOUN', 'street': 'NOUN', 'inch': 'NOUN', 'lot': 'NOUN', 'nothing': 'PRON', 'course': 'NOUN', 'stay': 'NOUN', 'wheel': 'NOUN', 'full': 'ADJ', 'force': 'NOUN', 'blue': 'ADJ', 'object': 'NOUN', 'decide': 'NOUN', 'surface': 'NOUN', 'deep': 'ADJ', 'moon': 'NOUN', 'island': 'NOUN', 'foot': 'NOUN', 'yet': 'ADV', 'busy': 'ADJ', 'test': 'NOUN', 'record': 'NOUN', 'boat': 'NOUN', 'common': 'ADJ', 'gold': 'NOUN', 'possible': 'ADJ', 'plane': 'NOUN', 'age': 'NOUN', 'dry': 'NOUN', 'wonder': 'NOUN', 'laugh': 'NOUN', 'thousand': 'NUM', 'ago': 'ADV', 'ran': 'VERB', 'check': 'NOUN', 'game': 'NOUN', 'shape': 'NOUN', 'yes': 'INTJ', 'cool': 'X', 'miss': 'NOUN', 'brought': 'VERB', 'heat': 'NOUN', 'snow': 'NOUN', 'bed': 'NOUN', 'bring': 'VERB', 'sit': 'VERB', 'perhaps': 'ADV', 'fill': 'NOUN', 'east': 'NOUN', 'weight': 'NOUN', 'language': 'NOUN', 'among': 'ADP'}


class SRA:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def token_string(self,sentence):
        sentence = re.sub('[!?.]', '',sentence)
        parsed = sentence.split()
        for i in parsed:
            if len(i) < 3:
                parsed.remove(i)
        return parsed

    def ADJ_Noun_handler(self, parsed):
        adj,noun = [],[]
        for parse in parsed:
            if dict.get(parse) == 'NOUN':
                noun.append(parse)
            elif dict.get(parse) == 'ADJ' or dict.get(parse) == 'NUM':
                adj.append(parse)
        return adj,noun

    def remove_from_question(self,parsed,question):
        question = re.sub('[!?.]', '', question)
        question = question.split()
        for i in parsed:
            if i in question or i == 'year':
                parsed.remove(i)
        return parsed

    def solve(self, sentence, question):
        question = question.lower()

        pos_names = ['Serena', 'Andrew', 'Bobbie', 'Cason', 'David', 'Farzana', 'Frank', 'Hannah', 'Ida', 'Irene', 'Jim', 'Jose', 'Keith',
                     'Laura', 'Lucy', 'Meredith', 'Nick', 'Ada', 'Yeeling', 'Yan', 'friend', 'she','he']

        parsed = self.token_string(sentence)
        name_usage = [i for i in parsed if i in pos_names]
        time_found = [x for x in parsed if ':' in x]
        parsed = [i for i in parsed if i not in name_usage and i not in time_found]
        adj,noun = self.ADJ_Noun_handler(parsed)
        if 'who' in question and 'to' in question or 'who' in question and 'with' in question:
            if name_usage[-1].lower() in question:
                return name_usage[0]
            return name_usage[-1] if len(name_usage) > 1 else name_usage[0]
        elif 'who' in question:
            return name_usage[0]
        elif 'time' in question:
            return time_found[0]
        elif 'what' in question:
            if 'name' in question or 'color' in question:
                return adj[0]
            if len(noun)> 1:
                noun = self.remove_from_question(noun, question)
            return noun[0]
        elif 'how' in question and noun[0] in question:
            if dict[adj[0]] == 'NUM':
                noun = self.remove_from_question(noun, question)
                return adj[0] + ' ' + noun[0]
            return adj[0]
        elif 'how' in question and 'to' in question:
            if len(noun)> 1:
                noun = self.remove_from_question(noun, question)
            return noun[0]
        elif 'where' in question:
            if len(noun)> 1:
                noun = self.remove_from_question(noun, question)
            return noun[2] if len(noun) > 3 else noun[0]
        return noun[-1]


nlpAgent = SRA()

val = nlpAgent.solve('Irene brought a short note to Michael.','Who brought the note?')
assert val == 'Irene'