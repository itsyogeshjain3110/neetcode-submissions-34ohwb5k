class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                ans.append(subset.copy())
                return

            # exclude
            backtrack(i+1)

            # include
            subset.append(nums[i])
            backtrack(i+1)

            #backtrack
            subset.pop()

        backtrack(0)
        return ans
        