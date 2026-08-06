class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            pro = 1
            temp = n

            while temp > 0:
                pro *= temp % 10
                temp //= 10

            if pro % t == 0:
                return n

            n += 1