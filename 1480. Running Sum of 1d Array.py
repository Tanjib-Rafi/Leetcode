class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        
        a_list = []
        
        for i in range(len(nums)) :
            sum += nums[i]
            
            a_list.append(sum)
        
        return a_list
