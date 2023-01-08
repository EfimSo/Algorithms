# Given an array arr of unsorted numbers and a target sum,
# count all triplets in it such that arr[i] + arr[j] + arr[k] < target
# where i, j, and k are three different indices. Write a function to return the count of such triplets.

# for i in r(l(arr)):
#   find two numbers i, j such that arr[i] + arr[j] < target - arr[i]

def triplet_with_smaller_sum(arr: list[int], target: int):
    arr.sort()
    triplet_count = 0

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            if arr[left] + arr[right] < target - arr[i]:
                # since right is the biggest number in the working subarray, 
                # any index between left and right will be a valid triplet
                triplet_count += right - left   
                left += 1
            else:
                right -= 1

    return triplet_count            


def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()