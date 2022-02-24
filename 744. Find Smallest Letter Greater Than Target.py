class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if ord(target) < ord(i):
                return i
        return letters[0]   
    
#second solution(binary search):

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        a = letters
        low = 0
        high = len(a)-1
        ans = a[0]
        while(low<=high):
            mid = (low+high)//2
            if(a[mid]==target):
                low = mid+1
            elif(a[mid] > target):
                ans = a[mid]
                high = mid-1
            elif(a[mid] < target):
                low = mid+1
        return ans
