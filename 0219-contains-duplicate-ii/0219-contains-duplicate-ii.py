class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

       #""" for i in range(len(nums)):if k == nums[i]:return True  else :      return False
        n=set()
        for i in range(len(nums)):
            if nums[i] in n :
                return True 
            else :
                n.add(nums[i])
            if len(n) >k :
                n.remove(nums[i-k])
        return False 