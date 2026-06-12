class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLen=0
        n = len(s)

        if n == 1: return s

        for i in range(n):
            # Odd
            l,h=i,i
            
            while l>=0 and h<n and s[l]==s[h]:
                if h-l+1 > resLen:
                    res = s[l:h+1]
                    resLen = h-l+1
                
                l-=1
                h+=1

            # Even
            l,h=i,i+1

            while l>=0 and h<n and s[l]==s[h]:
                if h-l+1>resLen:
                    res=s[l: h+1]
                    resLen=h-l+1
                
                l-=1
                h+=1

        return res
