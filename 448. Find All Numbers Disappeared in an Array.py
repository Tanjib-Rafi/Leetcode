class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        highest = len(nums)
        ll = []
        nums = set(nums)
        for i in range(1,highest+1):
            if i not in nums:
                ll.append(i)
        return ll
        
