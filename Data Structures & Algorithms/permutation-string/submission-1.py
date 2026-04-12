class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1 = [0]*26
        for i in s1:
            count_s1[ord(i) - ord('a')]+=1
        
        l = 0
        r = 0
        count_s2 = [0]*26
        while r < len(s2):
            if r-l >= len(s1):
                count_s2[ord(s2[l]) - ord('a')]-=1
                l+=1
            count_s2[ord(s2[r]) - ord('a')]+=1
            if count_s1 == count_s2:
                return True
            r+=1
        print(count_s1)
        print(count_s2)
        return False



        
        