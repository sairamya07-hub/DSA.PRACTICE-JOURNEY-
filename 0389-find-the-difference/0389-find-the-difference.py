class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)
        for i in range (n):
            for j in range (m):
                if s[i]==t[j]:
                    t=t[:j]+t[j+1:]
                    break 
        return t