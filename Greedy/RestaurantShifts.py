# Given a list of shifts in a restaurant with [s, f] being the start and finish time of the shift,
# find the minimal set of shifts so that there's at least one person working at each point
def find_min_shifts(shifts):
    shifts.sort(key=lambda x: x[1]) # sort by finish time
    # pick next shift to ensure that the start time of the next shift is at least the finish time of the previous
    # pick the shift with the latest finish time that still overlaps with previous finish time
    res = []
    s_prev, f_prev = shifts[0] # last covered shift
    res.append(shifts[0])
    s_curr, f_curr = None, None # last seen shift
    for s, f in shifts:
        if s >= f_prev and s_curr is not None: # intervals are open at the end so s == f_prev is valid
            res.append([s_curr, f_curr])
            f_prev = f_curr    # update last covered finish time
        s_curr, f_curr = s, f
    res.append([s_curr, f_curr])
    return res

# Given the list of shifts, find the maximum number of visits 
# such that each visit only overlaps with each shift once
# Intervals are closed at the start time and open at end time
def find_visits(shifts):
    min_schedule = find_min_shifts(shifts)
    res = []
    res.append(min_schedule[0][0])
    for _, f in min_schedule:
        res.append(f)
    return res[:-1]     # exclude end of last interval since no shift at end

l = [[0, 0.5], [0.3, 0.7], [0.4, 1], [0.6, 1.8], [1.4, 1.7]]
print(find_min_shifts(l))
print(find_visits(l))


# Online Python - IDE, Editor, Compiler, Interpreter

class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return "(" + str(self.key) + "," + str(self.val) + ")"

def find_smaller(root, t):
    if not root or root.key >= t:
        return []
    res = [root]
    res += find_smaller(root.left, t)
    res += find_smaller(root.right, t)
    return res

def main():
    n1 = Node(3, 4)
    n1.left = Node(5, 1)
    n1.right = Node(6, 4)
    n1.left.left = Node(7, "idk")
    n1.right.left = Node(10, 8)
    n1.right.right = Node(7, 5)
    print(find_smaller(n1, 6))
main()
