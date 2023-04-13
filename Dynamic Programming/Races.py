# You are training for the Boston Marathon by running various shorter races.
# There is one race every week. You have developed your own point system where for each race you
# award yourself a number of fitness points, based on how much you will gain from doing that race. Plan out
# which races to run so that you are as fit as possible by Marathon Day. As input you get the dates of the n
# races and the amount of points for each day in a table F. Design a dynamic programming algorithm for the
# below problems.
from functools import lru_cache
# import time
# 1. Design your schedule if you can’t run two weeks in a row.
def races_schedule1(races: list[int]):
    memo = {}
    # @lru_cache
    def recur(i):
        if i < 0:
            return 0
        if i not in memo:
            memo[i] = max(races[i] + recur(i-2), recur(i-1))
        return memo[i]
    return recur(len(races)-1), memo
def races_trace1(races, schedule):
    res = []
    schedule[-2], schedule[-1] = 0, 0
    def recur(i):
        if i < 0:
            return 0
        if races[i] + schedule[i-2] > schedule[i-1]:
            res.append(races[i])
            recur(i-2)
        else:
            recur(i-1)
    recur(len(races)-1)
    return res
schedule = [1, 10, 15, 10, 3]

# 2. Design your schedule if you can run at most two weeks in a row and then have to rest a week.
def races_schedule2(races):
    # two dimensional OPT(i, j) where i is the index of the race and j is the number of consecutive races ran
    memo = {} 
    def dp(i):
        if i in memo:
            return memo(i)
        if i < 0:
             return 0
        if i == 0:
            return races[0]
        if i == 1:
            return races[0] + races[1]
        if i == 2:
            return max(races[0] + races[1], races[1] + races[2], races[0] + races[2])
        memo[i] = max(races[i] + dp(i-2), races[i] + races[i-1] + dp(i-3), dp(i-1))
        return memo[i]
    return dp(len(races))
    
    
    
    
# def dp(i, j):
#     if i <= 0:
#         return 0
#     if (i, j) in memo:
#         return memo[(i, j)]
    