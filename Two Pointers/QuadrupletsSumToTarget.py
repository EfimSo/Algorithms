# Given an array of unsorted numbers and a target number,
# find all unique quadruplets in it, whose sum is equal to the target number.


def search_quadruplets(arr, target):
    arr.sort()
    result = []
    for i in range(len(arr) - 3):
        for j in range(i + 1, len(arr) - 2):
            left = j + 1
            right = len(arr) - 1
            while left < right:
                cur_sum = arr[i] + arr[j] + arr[left] + arr[right]
                if  cur_sum == target:
                    result.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1
    return result

def main1():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))

# main1()

# version with code that skips duplicates

def search_quadruplets_dup(arr, target):
    arr.sort()
    result = []
    for i in range(len(arr) - 3):
        if i > 0 and arr[i] == arr[i - 1]:      # skip duplicates outer loop
            continue
        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:      # skip duplicates inner loop
                continue
            left = j + 1
            right = len(arr) - 1
            while left < right:
                cur_sum = arr[i] + arr[j] + arr[left] + arr[right]
                if  cur_sum == target:
                    result.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left - 1]:      # skip duplicates left
                        left += 1
                    while left < right and arr[right] == arr[right + 1]:    # skip duplicates right
                        right -= 1
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1
    return result

def main2():
    print(search_quadruplets_dup([4, 1, 1, 1, 2, 2, -1, 1, -3], 1))
    print(search_quadruplets_dup([2, 0, -1, 1, -2, -2, 2, 2], 2))

main2()