# Input: array of positive integers. For each integer m, move m indeces forward or backwards
# Since array is circular, if reached end of the array, continue from 0
# Similarly, if reached beginning while traveling backwards, continue from last index
# Method to determine if the array has a cycle. 
# The cycle should have more than one element and should follow one direction 
# which means the cycle should not contain both forward and backward movements.

def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        is_forward = arr[i] >= 0 # direction 
        slow, fast = i, i
        while True:
            slow = find_next_index(arr, is_forward, slow)   # move slow 1 step
            fast = find_next_index(arr, is_forward, fast)   # move fast 1 step
            if fast != -1:
                fast = find_next_index(arr, is_forward, fast)   # move fast another step if valid ind
            if slow == -1 or fast == -1 or fast == slow:
                break
        if slow != -1 and slow == fast:     # met at a valid index - cycle exists
            return True
    return False


def find_next_index(arr, is_forward, curr_index):
    direction = arr[curr_index] >= 0
    if direction != is_forward:
        return -1   # since cycle can only contain one direction, break if detected a change in dir
    
    next_index = (curr_index + arr[curr_index]) % len(arr)
    if next_index == curr_index:
        return -1   # break if one element cycle
    return next_index

def main():
  print(circular_array_loop_exists([1, 2, -1, 2, 2]))
  print(circular_array_loop_exists([2, 2, -1, 2]))
  print(circular_array_loop_exists([2, 1, -1, -2]))


main()