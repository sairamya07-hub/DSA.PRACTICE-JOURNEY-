class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if(char in "{[("):
                stack.append(char)
            else:
                if (len(stack)==0):
                    return False
                x=stack.pop()
                if((x =="(" and char ==")")or(x =="{" and char =="}")or(x =="[" and char=="]")):
                    continue 
                else:
                    return False
        return len(stack)==0
        