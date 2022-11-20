import hashlib
import math
import random


#Chinese Remainder theorem used in cryptography
class ChineseRemainder:

    def __init__(self):
        pass

    '''
    psuedo code for egcd and inverse function can be found at https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    Under the Python Section.
    These are also a good source of where i've got the knowledge from https://cp-algorithms.com/algebra/module-inverse.html#toc-tgt-1 
    and https://cp-algorithms.com/algebra/extended-euclid-algorithm.html

    '''
    def egcd(self, e, totient):
        if e == 0:
            #Found our gcd and x ,y such that d = a * x  + b * y = totient = gcd(a,b)
            return (totient, 0, 1)
        else:
            #recursively call egcd until i've found the right gcd
            gcd, b, a = self.egcd(totient % e, e)
            return gcd, a - b*(totient // e), b
        
    def inverse(self,e, totient):
        gcd,x,y = self.egcd(e, totient)
        if gcd == 1:  
            return x%totient 
        return math.nan #Return this if i've found an undefined or unpresentable number. 

    '''
    psuedo code for binary search can be found at https://stackabuse.com/binary-search-in-python/
    under the iterative section.

    '''
    def binarySearch(self, tot : int):
        start=0
        end = tot
        while start < end:
            mid = (start+end)//2
            if pow(mid,3) < tot:
                start = mid+1
            else:
                end = mid
        return start

    def chineseRemainder(self, n_1_str: str, c_1_str: str, n_2_str: str, c_2_str: str, n_3_str: str, c_3_str: str):
        n_1 = int(n_1_str, 16)
        c_1 = int(c_1_str, 16)
        n_2 = int(n_2_str, 16)
        c_2 = int(c_2_str, 16)
        n_3 = int(n_3_str, 16)
        c_3 = int(c_3_str, 16)

        msg = ''
        m = 0

        totN = n_1 * n_2 * n_3

        #Find n such that it Ni is not included
        #Chinese Remainder theorem
        ciphers = [c_1,c_2,c_3]
        N = [n_1,n_2,n_3]
        
        n = [totN//n_1, totN//n_2, totN//n_3]
        a = [self.inverse(n[i],N[i]) for i in range(len(ciphers))]
        c = [n[i]*ciphers[i]*a[i] for i in range(len(ciphers))]
        
        total = 0
        for i in c:
            total+=i
        res = total%totN

        m = self.binarySearch(res)
        

        # Solve for m, which is an integer value, the line below will convert it to a string:
        msg = bytes.fromhex(hex(m).rstrip('L')[2:]).decode('UTF-8')

        return msg
