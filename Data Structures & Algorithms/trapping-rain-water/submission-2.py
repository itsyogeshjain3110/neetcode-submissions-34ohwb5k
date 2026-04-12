class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        maxL,maxR = 0,0
        trapped_water = 0
        while l<r:
            if height[l] < height[r]:
                #maintain maxL
                if height[l] >= maxL:
                    maxL = height[l]
                else:
                    trapped_water += (maxL - height[l])
                l+=1

            else:
                #maintain maxR
                if height[r] >= maxR:
                    maxR = height[r]
                else:
                    trapped_water += (maxR - height[r])
                r-=1
        return trapped_water
