class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        a=len(g)
        b=len(s)
        l=0
        r=0
        count =0
        while l<a and r<b:
            if g[l]<=s[r]:
                count+=1
                l=l+1
            r=r+1
        return count 
