class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : 
          return False
        
        s_dict = {}
        t_dict = {}
        
        for character in range(len(s)) : #counting values in s and t
            s_dict[s[character]] = 1 + s_dict.get(s[character] , 0) #if key doesn't exist set default 0
            t_dict[t[character]] = 1 + t_dict.get(t[character] , 0)
            
        for count in s_dict:
            if s_dict[count] != t_dict.get(count, 0 ):
                return False
        return True
