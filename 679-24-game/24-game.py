class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        EPS = 1e-6

        def backtrack(nums):
            # Only one number left
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS

            # Pick every pair
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):

                    # Numbers not selected
                    remaining = [
                        nums[k]
                        for k in range(len(nums))
                        if k != i and k != j
                    ]

                    a = nums[i]
                    b = nums[j]

                    # All possible results
                    results = [
                        a + b,
                        a - b,
                        b - a,
                        a * b
                    ]

                    if abs(b) > EPS:
                        results.append(a / b)

                    if abs(a) > EPS:
                        results.append(b / a)

                    # Try every operation
                    for result in results:
                        remaining.append(result)

                        if backtrack(remaining):
                            return True

                        remaining.pop()

            return False

        return backtrack([float(x) for x in cards])