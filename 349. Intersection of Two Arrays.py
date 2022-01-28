class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      
        a_set = set()
        
        for i in nums1 :
            
            if i in nums2 :
                   
                a_set.add(i)
                
        return a_set


#second solution:

# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

#         a_set = set(nums1) & set(nums2)

#         return a_set
