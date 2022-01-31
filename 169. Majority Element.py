class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for n in nums:
            if count == 0:
                res = n
            if res == n:
                count+=1
            else:
                count-=1
        return res           

    
#hashmap solution:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res,maxCount = 0,0
        
        for n in nums:
            count[n]= 1 + count.get(n,0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)
        return res
