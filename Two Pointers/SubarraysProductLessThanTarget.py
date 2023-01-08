# Given an array with positive numbers and a positive target number,
# find all of its contiguous subarrays whose product is less than the target number.

# sliding window

from collections import deque

def find_subarrays(arr, target):
    window_start, window_product = 0, 1
    res_arr = []

    for window_end in range(len(arr)):
        window_product *= arr[window_end]

        while window_product >= target and window_start < len(arr):
            window_product /= arr[window_start]
            window_start += 1
        
        # since all subarrays between window_start and window_end will have product < target,
        # we need to append all subarrays between window_start and window_end to the result array
        temp_list = deque()
        for i in range(window_end, window_start-1, -1):
            temp_list.appendleft(arr[i])
            res_arr.append(list(temp_list))

    return res_arr

def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))


main()