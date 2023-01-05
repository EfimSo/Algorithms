# Given an array of sorted numbers and a target sum, 
# find a pair in the array whose sum is equal to the given target.

# approach using two pointers: O(n) time O(1) space
def twosum_tp(nums, target):
    left, right = 0, len(nums) - 1
    
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        if sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]

# approach using hashmap: O(n) time O(n) space
def twosum_hm(nums, target):
    num_dict = dict()
    for i, num in enumerate(nums):
        if target - num in num_dict:
            return [num_dict[target - num], i]
        num_dict[num] = i
    return [-1, -1]


def main():
#   print(twosum_tp([1, 2, 3, 4, 6], 6))
#   print(twosum_tp([2, 5, 9, 11], 11))
    print(twosum_hm([1, 2, 3, 4, 6], 6))
    print(twosum_hm([4, 3, 2, 5, 9, 11], 11))


main()