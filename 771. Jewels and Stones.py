class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a_set = set(jewels)
        count = 0
        for i in range(len(stones)):
            if stones[i] in a_set:
                count+=1
        return count

#second solution:
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for s in jewels:
            count += stones.count(s) #at first checking how many a in stones jewels = "aA", stones = "aAAbbbb"
        return count
