# Write a generator which takes a list (or any sequence)
# and returns items from the list in random order.
import numpy as np

def randomized(seq):
    """Iterate over seq returning items in random order.

    Making a copy of the argument or mutating the argument is *not
    allowed*.

    >>> list(randomized('abcdefghi'))
    ['b', 'a', 'e', 'd', 'f', 'c', 'h', 'i', 'g']
    """
    #import pdb
    #pdb.set_trace()
    while len(seq)>0:
        idx = np.random.randint(0,len(seq))
        yield seq[idx]
        seq = seq[:idx] + seq[idx+1:]    

if __name__=="__main__":
    seq = "abcdefg"
    
    for i in randomized(seq): print i
