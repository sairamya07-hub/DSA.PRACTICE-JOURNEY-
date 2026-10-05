class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans=[0]
        for i in s :
            if i=="(":
                ans.append(0)
            else:
                k=ans.pop()
                l=ans.pop()
                ans.append(l+max(2*k,1))
        return ans.pop()