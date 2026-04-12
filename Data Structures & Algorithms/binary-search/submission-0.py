class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # -1,0,2,4,6,8
        # 0,1,2,3,4,5
        # 
        l  = 0
        r = len(nums) - 1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid -1
            else:
                return mid
        return -1 
        