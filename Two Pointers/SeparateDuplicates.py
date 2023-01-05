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

def main():
  l1 = [2, 3, 3, 3, 6, 9, 9]
  l2 = [2, 2, 2, 11]
  print(remove_duplicates(l1))
  print(l1)
  print(remove_duplicates(l2))
  print(l2)

main()