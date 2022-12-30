# Given an array containing 0s and 1s, 
# if you are allowed to replace no more than k 0s with 1s,
# find the length of the longest contiguous subarray having all 1s.

def findLongestOnes(nums, k):
    window_start, max_len, max_ones = 0,0,0

    for window_end in range(len(nums)):
        # update number of 1s in window
        if nums[window_end] == 1:
            max_ones += 1
        # if number of 0s is more than k, shrink window
        if (window_end - window_start + 1 - max_ones) > k:
            if nums[window_start] == 1:
                max_ones -= 1
            window_start += 1
        max_len = max(max_len, window_end - window_start + 1)
    
    return max_len


print(findLongestOnes([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(findLongestOnes([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))