class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count = 0

        for i in range(len(nums)) :

            if(nums[i] != val) :
                nums[count] = nums[i]
                count = count + 1

        return count
