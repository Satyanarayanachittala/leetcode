class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)

        ans = []

        for i in range(1, 101):
            count = (i in s1) + (i in s2) + (i in s3)
            if count >= 2:
                ans.append(i)

        return ans