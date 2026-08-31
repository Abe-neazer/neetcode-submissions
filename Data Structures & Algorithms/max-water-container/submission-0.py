class Solution:
    def maxArea(self, heights: List[int]) -> int:

        R = len(heights)-1
        L = 0
        Max_Area = 0

        while L < R:
            h = min(heights[L],heights[R])
            w = R - L

            a = h * w

            Max_Area = max(Max_Area, a)

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return Max_Area


        