class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i] :
                max_area = max((i-stack[-1][0])*stack[-1][1], max_area)
                start = stack[-1][0]
                stack.pop()
            stack.append([start, heights[i]])
        for ele in stack:
            max_area = max((len(heights)-ele[0])*ele[1], max_area)

        return max_area
        