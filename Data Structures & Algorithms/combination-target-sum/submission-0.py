class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(i, curr, total):
            if total == target:
                ans.append(curr.copy())
                return

            if i >= len(nums) or total > target:
                return


            backtrack(i+1,curr,total)

            curr.append(nums[i])
            backtrack(i,curr,total+nums[i])

            curr.pop()



        
        backtrack(0, [], 0)

        return ans
        