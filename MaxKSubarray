
# find maximum sum of contiguous subarray of size k using the sliding window technique
# time complexity: O(n), space complexity: O(1), previously O(n) with a list

def findMaxSub(nums, k):
    max_sum, window_sum, window_start = 0, 0, 0
    for window_end in range(len(nums)):
        window_sum += nums[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[window_start]
            window_start += 1
    return max_sum

input1 = [2, 1, 5, 1, 3, 2]
input2 =  [2, 3, 4, 1, 5]

print(findMaxSub(input1, 3))
print(findMaxSub(input2, 2))

    