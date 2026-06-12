class Solution:
    def countSubstrings(self, s: str) -> int:
        res=[]
        n = len(s)

        if n==1: return n

        for i in range(n):
            #odd
            l,h=i,i

            while l>-1 and h<n and s[l]==s[h]:
                res.append(s[l:h+1])
                l-=1
                h+=1

            #even
            l,h=i,i+1
            while l>-1 and h<n and s[l]==s[h]:
                res.append(s[l:h+1])
                l-=1
                h+=1
        
        return len(res)