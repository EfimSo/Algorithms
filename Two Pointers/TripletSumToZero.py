# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
# x + y + z == 0 -> x + y == -z
# Time complexity: sort + alogrithm == O(nlog(n) + n * n) == O(n^2)
# Space complexity: excluding output array, O(n) required for sorting (worst case)

def search_triplets(arr):
    arr.sort()          # sort array
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:      # skip duplicates
            continue
        search_pair(arr, -arr[i], i + 1, triplets)
    return triplets

def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while left < right:
        cur_sum = arr[left] + arr[right]
        if cur_sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:      # skip duplicates left pointer
                left += 1
            while left < right and arr[right] == arr[right + 1]:    # skip duplicates right pointer
                right -= 1

        elif cur_sum < target_sum:
            left += 1
        else:
            right -= 1
    

def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()