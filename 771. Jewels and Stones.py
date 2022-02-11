class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a_set = set(jewels)
        count = 0
        for i in range(len(stones)):
            if stones[i] in a_set:
                count+=1
        return count
