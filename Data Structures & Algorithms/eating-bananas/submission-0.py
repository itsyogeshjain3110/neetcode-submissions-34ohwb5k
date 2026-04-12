class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = float("inf")
        while l<=r:
            curr_hour = 0
            banana_to_eat = (l+r)//2
            for curr_pile in piles:
                curr_hour+=math.ceil(curr_pile / banana_to_eat)
            print(l,r,banana_to_eat,curr_hour)
            if curr_hour <= h:
                k = min(k,banana_to_eat)
                r = banana_to_eat - 1
            else:
                l = banana_to_eat + 1
            
        return k




        