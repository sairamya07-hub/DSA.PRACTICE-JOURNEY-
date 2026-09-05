class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
     #   count = 0
     #   prefixSum = 0
     #   seen = {0:1} 
     #   for num in nums:
     #       prefixSum += num
     #       if prefixSum - k in seen:
     #           count += seen[prefixSum - k]
     #       seen[prefixSum] = seen.get(prefixSum, 0) + 1
     #   return count
          count=0
          sum=0
          d={0:1}
          for i in range(0,len(nums)):
              sum+=nums[i]
              if sum-k in d:
                count+=d[sum-k]
              if(sum in d):
                d[sum]+=1
              else:
                 d[sum]=1
          return count