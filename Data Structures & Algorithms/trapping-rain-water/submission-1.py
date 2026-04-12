class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_array = []
        max_left = float("-inf")
        for i in height:
            max_left_array.append(max_left)
            max_left = max(max_left,i)

        print("max_left_array", max_left_array)

        max_right_array = []
        max_right = float("-inf")
        for i in height[::-1]:
            max_right_array.append(max_right)
            max_right = max(max_right,i)
        max_right_array = max_right_array[::-1]

        print("max_right_array", max_right_array)
        trapped_water = 0
        for i in range(1,len(height)-1):
            water=(min(max_left_array[i],max_right_array[i]) - height[i])
            if water > 0:
                trapped_water+=water
                

        return trapped_water