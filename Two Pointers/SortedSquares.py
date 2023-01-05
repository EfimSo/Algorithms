# Given a sorted array, return a new array containing squares of all the numbers of the input array in the sorted order.

def make_squares(nums):
    n = len(nums)
    squares = [0 for x in range(n)]
    biggest_square = n - 1 # pointer for index of last and largest square (last since sorted)
    left, right = 0, n - 1
    while left <= right:
        left_square = nums[left] * nums[left]
        right_square = nums[right] * nums[right]
        if left_square > right_square:
           squares[biggest_square] = left_square
           left += 1
        else:
            squares[biggest_square] = right_square
            right -= 1
        biggest_square -= 1
    return squares


def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()