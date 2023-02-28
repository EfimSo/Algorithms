# Given a list of shifts in a restaurant with [s, f] being the start and finish time of the shift,
# find the minimal set of shifts so that there's at least one person working at each point


def find_min_shifts(shifts):
    shifts.sort(key=lambda x: x[1]) # sort by finish time
    # pick next shift to ensure that the start time of the next shift is at least the finish time of the previous
    # pick the shift with the latest finish time that still overlaps with previous finish time
    res = []
    s_prev, f_prev = shifts[0] # last uncovered shift
    res.append(shifts[0])
    s_curr, f_curr = None, None # last seen shift
    for s, f in shifts:
        if s >= f_prev and s_curr is not None: # intervals are open at the end so s == f_prev is valid
            res.append([s_curr, f_curr])
            s_prev, f_prev = s, f
        s_curr, f_curr = s, f
    if res[-1] == [s_curr, f_curr]: # encountered non-overlapping shift that needs to be added to res
       res.append([s_prev, f_prev])
    else:
       res.append([s_curr, f_curr]) # did not ecounter non-overlapping shift so last compatible shift
                                    # needs to be added to the result
 
    return res

# Given the list of shifts, find the maximum number of visits 
# such that each visit only overlaps with each shift once
# Intervals are closed at the start time and open at end time
def find_visits(shifts):
    min_schedule = find_min_shifts(shifts)
    res = []
    res.append(min_schedule[0][0])
    for s, f in min_schedule:
        res.append(f)
    return res

l = [[0, 0.5], [0.3, 0.7], [0.4, 1], [0.6, 2], [2, 2.5]]
print(find_min_shifts(l))
print(find_visits(l))