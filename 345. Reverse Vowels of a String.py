class Solution:
    def reverseVowels(self, s: str) -> str:
        a=list(s) #string is immutable so converting to list
        
        vowels={"a","e","i","o","u","A","E","I","O","U"}
        
        l=0
        r=len(a)-1
        
        while(l<r):
            
            if(a[l] not in vowels):
                l+=1
                
            if(a[r] not in vowels):
                r-=1
                
            if(a[l] in vowels and a[r] in vowels):
                a[l],a[r]=a[r],a[l]
                
                l+=1
                r-=1
                
        return(''.join(a))

        
