# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
# return the maximum number of points that lie on the same straight line.

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        max_points = 0
        if len(points) == 1:
            return 1
        for x, y in points:
            slopes = dict()
            for x_, y_ in points:
                if x == x_ and y == y_:
                    continue
                if y - y_ != 0:
                    slope = (x - x_) /(y - y_)
                else:
                    slope = float('inf')
                if slope not in slopes:
                    slopes[slope] = 0
                slopes[slope] += 1
            if slopes.values():
                maxp = max(slopes.values()) + 1
                max_points = max(max_points, maxp)
        return max_points
                