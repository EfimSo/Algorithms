# Given a list of tasks with [s, f] being the start and finish time of the task,
# Find the max number of non overlapping tasks
class Solution:
    # @param A: list of list of ints
    # @return: int
    def find_intervals(self, A):
        A.sort(key=lambda x: x[1])
        count = 1
        s_prev, f_prev = A[0]
        for s, f in A:
            if s > f_prev:
                s_prev, f_prev = s, f
                count += 1
        return count
s = Solution()
print(s.find_intervals([[1, 2], [2.5, 3], [4, 6], [3, 6], [0, .99]]))