class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count  = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        final = [[] for i in range(len(nums)+1)]
        for i in count:
            final[count[i]].append(i)

        output = []
        for lst in final[::-1]:
            for i in lst:
                if k == 0:
                    return output
                output.append(i)
                k-=1 
        
        return output