class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = 1
        pre_array = []
        for i in nums:
            pre_array.append(pre)
            pre = pre*i
        print("pre array",pre_array)
        post = 1
        post_array = []
        for i in nums[::-1]:
                post_array.append(post)
                post*=i
        post_array = post_array[::-1]
        print("post array", post_array)
        for i in range(len(nums)):
            res.append(pre_array[i]*post_array[i])
        return res



        