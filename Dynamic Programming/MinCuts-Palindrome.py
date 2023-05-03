# Given a string, return the minimum number of cuts that need to be made 
# to create a partion where every string in the partition is a palindrome
# min_cut("cbba") = 2, min_cut("aa") = 0
from math import inf
def min_cut(s):
    n = len(s)
    # Keeps track of the number of cuts needed to partition C[i][j]
    C = [[inf for i in range(n)] \
            for i in range(n)] 
    # P[i][j] = True if s[i:j+1] is a palindrome
    P = [[False for i in range(n)] \
                for i in range(n)]  
    for i in range(n):
        # set base cases for len of 1
        C[i][i] = 0
        P[i][i] = True
        # set base cases for len of 2
        if i > 0:
            if s[i] == s[i-1]:
                C[i-1][i] = 0
                P[i-1][i] = True
            else:
                C[i-1][i] = 1
        if i < n-1:
            if s[i] == s[i+1]:
                C[i][i+1] = 0
                P[i][i+1] = True
            else:
                C[i][i+1] = 1
    return C, P
C, P = min_cut("aabba")
for i in range(len(C)):
    for j in range(len(C[0])):
        print(C[i][j], end=" ")
    print()