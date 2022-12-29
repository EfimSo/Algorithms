# given int list nums and int k
# find the length of the smallest contigous subarray with sum >= k
import math

def findSmallestOverK(nums: list[int], k: int) -> int:
    windowSum, windowStart = 0, 0
    smallest = math.inf                     # intialize smallest to infinity

    for windowEnd in range(len(nums)):
        windowSum += nums[windowEnd]        # grow window
        # shrink window until not >= k
        while windowSum >= k:
            smallest = min(smallest, windowEnd - windowStart + 1)
            windowSum -= nums[windowStart]
            windowStart += 1
    
    if smallest == math.inf:
        return 0
    return smallest

input1 = [2, 1, 5, 2, 3, 2]
print(findSmallestOverK(input1, 7)) # should be 2

input2 = [2, 1, 5, 2, 8]
print(findSmallestOverK(input2, 7)) # should be 1

input3 = [3, 4, 1, 1, 6]
print(findSmallestOverK(input3, 8)) # should be 3
