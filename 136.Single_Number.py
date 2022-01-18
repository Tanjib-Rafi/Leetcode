#First way::

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]# popitem(): Remove the last item from the dictionary
    
#Second way::
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums):
                if nums[i] not in nums[i+1:]:
                    return nums[i]
                else:
                    i += 2
