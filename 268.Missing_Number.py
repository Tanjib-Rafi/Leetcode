class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        highest = max(nums)
        for i in range(highest+2):
            if i not in nums:
                return i
