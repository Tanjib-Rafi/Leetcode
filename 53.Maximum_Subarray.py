class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_val = max_val = float("-inf") #negative infinity number
        for n in nums:
            curr_val = max(n, n+curr_val)
            max_val = max(curr_val,max_val)
        return max_val