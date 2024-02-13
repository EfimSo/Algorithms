
# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Constraints:
#  - at least two elements in the array
#  - are there negative elements?
#  - can walls hold water?
#  - do elements in the middle affect the amount of water? 


def maxArea(heights: list[int]) -> int:
    i, j = 0, len(heights) - 1
    max_area = 0
    while i < j:
        a, b = heights[i], heights[j]
        area = min(a, b) * (j - i)
        max_area = max(area, max_area)
        if a <= b:
            i += 1
        else:
            j -= 1
    return max_area

# test)
tc = [1,8,6,2,5,4,8,3,7]
assert maxArea(tc) == 49
print("Test case passed")