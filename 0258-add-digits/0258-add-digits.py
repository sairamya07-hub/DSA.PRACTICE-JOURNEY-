class Solution:
    def addDigits(self, num: int) -> int:
        s=(num-1)%9
        if num==0:
            return 0 
        else :
            return s+1
