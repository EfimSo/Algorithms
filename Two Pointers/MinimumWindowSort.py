# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
import math

def shortest_window_sort(arr):
    left, right = 0, len(arr) - 1
    # Find first elements out of order on left and right (iterate while ascending order is preserved)
    # Then arr[left: right + 1] is the working subarray
    while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
        left += 1
    
    if left == len(arr) - 1:        # array is already sortred
        return 0

    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1
    
    # Find min and max of the working subarray
    subarray_max = -math.inf
    subarray_min = math.inf
    for i in range(left, right + 1):
        subarray_max = max(subarray_max, arr[i])
        subarray_min = min(subarray_min, arr[i])
    
    # extend subarray from beginning to include any number bigger than the minimum of the subarray
    # and from the end to include any number any number smaller than the subarray max
    # we know numbers left and right of the subarray are sorted since left and right are first ones out of order
    while left > 0 and arr[left - 1] > subarray_min:
        left -= 1
    while right < len(arr) - 1 and arr[right + 1] < subarray_max:
        right += 1
    
    return right - left + 1


def main():
  print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
  print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
  print(shortest_window_sort([1, 2, 3]))
  print(shortest_window_sort([3, 2, 1]))


main()
