# Given an array of sorted numbers,
# remove all duplicate number instances from it in-place, such that each element appears only once.
# 
# Move all the unique elements at the beginning of the array and 
# return the length of the subarray that has no duplicate in it. 

def remove_duplicates(arr):
    i, nextNonDuplicate = 0, 1 # working index, index one after sorted unique array
    while i < len(arr):                                 # for (int i = 0, i < arr.length, i++) 
        if arr[nextNonDuplicate - 1] != arr[i]:         
            arr[nextNonDuplicate] = arr[i]               
            nextNonDuplicate += 1                       
        i += 1
    return nextNonDuplicate

# given a list remove all instances of key by moving non-key elems to the front and
# returning length of the subarray with no instances of key

def remove_key(arr, key):
    next_not_key = 0 # pointer to the last confirmed non-key element
    i = 0
    while i < len(arr):
        if arr[i] != key:
            arr[next_not_key] = arr[i]
            next_not_key += 1
        i += 1
    return next_not_key

def main1():
  l1 = [2, 3, 3, 3, 6, 9, 9]
  l2 = [2, 2, 2, 11]
  print(remove_duplicates(l1))
  print(l1)
  print(remove_duplicates(l2))
  print(l2)

# main1()

def main2():
  l1 = [3, 2, 3, 6, 3, 10, 9, 3]
  print(remove_key(l1, 3))
  print(l1)
  l2 = [2, 11, 2, 2, 1]
  print(remove_key(l2, 2))
  print(l2)


main2()
