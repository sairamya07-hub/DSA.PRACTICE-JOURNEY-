class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        fa=0
        for i in range(left,right+1):
            a=bin(i)[2:]
            count=0
            for j in a:
                if j=='1':
                    count+=1
            ans=0
            for k in range(1,count+1):
                if count % k==0:
                    ans+=1
            if(ans==2):
                fa+=1
        return fa