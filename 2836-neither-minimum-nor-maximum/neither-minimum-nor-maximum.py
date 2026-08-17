class Solution:
    def findNonMinOrMax(self, nums):
        a=sorted(nums)
        k=((len(a)-1)//2)
        if k<1:
            return -1
        else:
            return a[k]
