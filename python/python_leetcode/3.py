class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for ch in t:
            if t.count(ch) != s.count(ch):
                return ch
            
            
sol=Solution()
print(sol.findTheDifference("ABCD","ABCDE"))