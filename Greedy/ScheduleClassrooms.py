# Given a list of tasks with [s, f] being the start and finish time of the task,
# Find the fewest number of classrooms to schedule all the tasks 
# with no two being assigned to the same classroom simultaniously
import heapq
# @param A: list of list of ints
# @return: int
def find_num_classrooms(A):
    tasks = []
    for s, f in A:
        tasks.append((s, 1))
        tasks.append((f, -1))
    tasks.sort()
    
    curr = 0 # classrooms currently used
    res = 0  # max classrooms used at any time
    for _, v in tasks:
        curr += v   # curr++ if starting time, curr-- if finish time 
        res = max(res, curr)
    return res

# @param tasks: list of [s, f] tasks
# @return: dict<classrooms, list of tasks assigned to classroom> 
# uses a min priority queue to keep track of classroom with earliest finish time
# runs in O(n log n)
# assumes closed intervals; change strict inequality in find_compatible_classroom to adjust
class Solution:
    def find_classrooms(self, tasks):
        A = dict()  # A[k] = list of courses assigned to room k
        Q = []      # empty list to be used as priority queue of (f, k) pairs 
                    # where f is finish time of last task assigned to k and k is classroom num
        sorted_tasks = sorted(tasks)
        for s, f in  sorted_tasks:
            k = self.find_compatible_classroom(s, Q) 
            if k is not None:
                A[k].append([s, f])
                heapq.heappush(Q, (f, k))   # push (finish time, k) in heap to update task assigned to k
            else:
                d = len(Q)          # current number of classrooms
                A[d + 1] = []       # open new classroom
                A[d + 1].append([s, f])
                heapq.heappush(Q, (f, d + 1))
        return A
    
    def find_compatible_classroom(self, start, Q):
        if not Q:
            return None
        f, k = heapq.heappop(Q)
        if start > f:
            return k
        else:
            heapq.heappush(Q, (f, k))    # restore entry since incompatible
            return None
    
    def print_tasks(self, tasks):
        A = self.find_classrooms(tasks)
        for k, l in A.items():
            print("classroom: ", k, " is assigned ", str(l))

