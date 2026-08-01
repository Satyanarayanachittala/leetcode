class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        def noZero(num):
            while num > 0:
                if num % 10 == 0:
                    return False
                num //= 10
            return True
        
        for a in range(1, n):
            b = n - a
            if noZero(a) and noZero(b):
                return [a, b]