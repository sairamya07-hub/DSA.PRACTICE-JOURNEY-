class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        maxs = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < maxs:
                return True
            while stack and stack[-1] < nums[i]:
                maxs = stack[-1]
                stack.pop()
            stack.append(nums[i])
        return False 