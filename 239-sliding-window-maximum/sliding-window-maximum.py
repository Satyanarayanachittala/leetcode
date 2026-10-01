from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        arr = []

        for i in range(len(nums)):

            # Remove index that is outside the current window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Once the first window is complete
            if i >= k - 1:
                arr.append(nums[dq[0]])

        return arr