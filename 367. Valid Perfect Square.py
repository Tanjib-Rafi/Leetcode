class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1,num+1) :
            if i**2 == num :
                return True
            if i**2 > num :
                return False
