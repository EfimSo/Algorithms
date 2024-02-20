# Randomized Quickselect implementation

# Problem:
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

import random
def findKthLargest(nums: list[int], k: int) -> int:
    k = len(nums) - k
    
    def quickselect(l, r):
        j = random.randint(l, r)
        nums[j], nums[r] = nums[r], nums[j]
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        if p > k: return quickselect(l, p-1)
        elif p < k: return quickselect(p+1, r)
        else: return nums[p]

    return quickselect(0, len(nums) - 1)
