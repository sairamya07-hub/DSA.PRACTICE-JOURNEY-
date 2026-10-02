class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        s=[""]*(n*2)
        ind=0
        cnt=0
        def par (ind,cnt):
            if ind >=len(s):
                if cnt==0:
                    ans.append("".join(s))
                return 

            if cnt>n:
                return 
            if cnt<0:
                return 
            s[ind]="("
            res=cnt+1
            par(ind+1,res)
            s[ind]=")"
            res=cnt-1
            par(ind+1,res)
        par(ind,cnt)
        return ans