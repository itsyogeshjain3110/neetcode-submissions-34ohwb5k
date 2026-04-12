class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = post = 1
        output = []
        
        for num in nums:
            output.append(pre)
            pre = num * pre

        for i in range(len(nums) - 1,-1,-1):
            output[i] = output[i] * post
            post = post * nums[i]
        
        return output