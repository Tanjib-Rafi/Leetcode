class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort(), nums2.sort()  # O(max(m, n) * log(max(m, n)))
        result = [] #output will be store in this list

        nums1_iterable, nums2_iterable  = 0, 0
        
        while nums1_iterable < len(nums1) and nums2_iterable < len(nums2):

            if nums1[nums1_iterable] < nums2[nums2_iterable]: #if nums1 value is smaller than nums2 , we will not put the value in list so iterate to the next value of nums1
                nums1_iterable += 1
            elif nums1[nums1_iterable] > nums2[nums2_iterable]: #if nums2 value is smaller than nums1, we will not put the value in the list so iterate to the next value of nums2 
                nums2_iterable += 1
            else: #if nums1 value equal to nums2 value ,store that value in result list and move on to the next value of nums1 and nums2
                result += nums1[nums1_iterable],
                nums1_iterable += 1
                nums2_iterable += 1

        return result