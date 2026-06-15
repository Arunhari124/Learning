class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x=sorted(s)
        y=sorted(t)
        for i in range(len(s)):
            if x[i] != y[i]:
                return (y[i])
        return (y[-1])
            
            
sol=Solution()
print(sol.findTheDifference("ABCD","ABCDE"))