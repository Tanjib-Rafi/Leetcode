class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = set()
        for i in nums:
            if i in table:
                return True
            else:
                table.add(i)
        return False

# if __name__ == "__main__":
    
#     List = [10, 5, 3, 4, 4, 6]
#     if (Solution.containsDuplicate(List)):
#         print("True")
#     else:
#         print("False")
