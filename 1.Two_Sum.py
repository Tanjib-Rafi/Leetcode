class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if((nums[i]+nums[j])==target):
                    return [i,j]
        return []


test_case = Solution()

array = [3, 2, 4]
print(test_case.twoSum(array, 6))

array = [2, 8, 11, 15]
print(test_case.twoSum(array, 9))
print(len(array))