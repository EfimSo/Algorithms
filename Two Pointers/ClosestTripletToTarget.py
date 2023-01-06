# Given an array of unsorted numbers and a target number, 
# find a triplet in the array whose sum is as close to the target number as possible,
# return the sum of the triplet.

# time complexity: sort + algorithm == O(nlogn) + O(n^2) == O(n^2)
# space complexity: O(n) —— worst case scenario for sorting 

import math

def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    min_diff = math.inf        # keep track of the smallest difference so far

    for i in range(len(arr) - 2):       # len - 2 since i, left and right have to be separate indeces
        left = i + 1
        right = len(arr) - 1
        while left < right:
            diff = target_sum - arr[i] - arr[left] - arr[right]
            if diff == 0:
                return target_sum
            if abs(diff) <  abs(min_diff) or abs(diff) == abs(diff) and diff > min_diff:    
                min_diff = diff
            if diff > 0:
                left += 1
            else:
                right -= 1
    return target_sum - min_diff

def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
    print(triplet_sum_close_to_target([0, 0, 1, 1, 2, 6], 5))


main()
