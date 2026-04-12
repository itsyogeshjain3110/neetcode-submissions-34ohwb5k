class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        output = float("inf")
        while l<=r:
            mid = (l+r)//2
            # check if left is unsorted
            output = min(output,nums[mid])
            # check if right is unsorted
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return output
