# Given an array containing 0s, 1s and 2s, sort the array in-place.
# You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.
# 
# The flag of the Netherlands consists of three colors: red, white and blue;
# and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

# two pointers: low, high = 0, len - 1
# while left < right:
#   put all the 0s before low and all the 2s after high.
#   left with sorted array (1s between low and high)

def dutch_flag_sort(arr):
    low, high = 0, len(arr) - 1
    i = 0
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else: # case for arr[i] == 2
            arr[i], arr[high] = arr[high], arr[i]
            # decrement high only, value at i could be any after swap 
            high -= 1



def main():
  arr = [1, 0, 2, 1, 0]
  dutch_flag_sort(arr)
  print(arr)

  arr = [2, 2, 0, 1, 2, 0]
  dutch_flag_sort(arr)
  print(arr)


main()
        