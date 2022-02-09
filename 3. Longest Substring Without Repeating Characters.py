class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in a_set: #there are 26 alphabets so O(n*26)==O(n) 
                a_set.remove(s[l])
                l+=1
            a_set.add(s[r])
            res = (max(res,len(a_set)))
        return res
