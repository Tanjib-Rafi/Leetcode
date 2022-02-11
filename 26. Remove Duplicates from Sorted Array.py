class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1 #because sorted we don't need to change the position of first value
        r = 1
        
        while r<len(nums) :
            if nums[r] != nums[r-1] :
                nums[l] = nums[r]
                l+=1
            r+=1
        return l
