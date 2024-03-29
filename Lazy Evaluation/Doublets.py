####################################################
#!/usr/bin/env python3
####################################################
import sys
sys.path.append('./../..')
from dictwords import word_is_legal
sys.path.append('./../../../../mypylib')
from mypylib_cls import *
####################################################
"""
HX-2023-03-24: 30 points
Solving the doublet puzzle
"""
####################################################
"""
Please revisit assign05_02.py.
######
Given a word w1 and another word w2, w1 and w2 are a
1-step doublet if w1 and w2 differ at exactly one position.
For instance, 'water' and 'later' are a 1-step doublet.
The doublet relation is the reflexive and transitive closure
of the 1-step doublet relation. In other words, w1 and w2 are
a doublet if w1 and w2 are the first and last of a sequence of
words where every two consecutive words form a 1-step doublet.
Here is a little website where you can use to check if two words
for a doublet or not:
http://ats-lang.github.io/EXAMPLE/BUCS320/Doublets/Doublets.html
######
Given a word, the function [doublet_stream_from] returns a stream
enumerating *all* the tuples such that the first element of the tuple
is the given word and every two consecutive words in the tuple form a
1-step doublet. The enumeration of tuples should be done so that shorter
tuples are always enumerated ahead of longer ones.
######
"""
from collections import deque # module that will be used for queue in BFS

def doublet_stream_from(word):
    # BFS search for doublets
    # at each step: 
    #   - pop word off a queue
    #   - find all children of the word and append to queue
    # ! Queue should hold paths instead of nodes for this problem (resolved cyclic path tracing)
    q = deque()
    q.append(word)
    def get_children(word):
        abc = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        for i, w in enumerate(word):
            for l in abc:
                if w == l:
                    continue
                word1 = word[:i] + l + word[i+1:]
                if word_is_legal(word1):
                    res.append(word1)
        # print(f"children: {res}")
        return res
    
    parents = {word: None}
    def trace_path(wrd):
        res = []
        curr = wrd
        while curr is not None:
            res.append(curr)
            curr = parents[curr]
        return tuple(res[::-1])
    
    def helper():
        if not q:
            return strcon_nil()
        wrd = q.popleft()
        for w in get_children(wrd):
            if w not in parents:
                q.append(w)
                parents[w] = wrd
        return strcon_cons(trace_path(wrd), helper)
    return helper
####################################################
