class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) 
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre*=nums[i]
        print("pre res",res)
        post = 1
        for i in range(len(nums)-1,-1,-1):
                res[i]*=post
                post*=nums[i]
        print("post res", res)
        return res



        