class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        l=0
        for i in range(0,n):
            if nums[i]>0 or nums[i]<0:
                nums[l],nums[i]=nums[i],nums[l]
                l=l+1
            