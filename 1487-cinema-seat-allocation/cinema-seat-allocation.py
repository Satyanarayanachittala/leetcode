class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}
        for row, seat in reservedSeats:
            rows[row] = rows.get(row, 0) | (1 << (seat - 1))
        ans = 2 * n
        LEFT = 0b0000011110
        MIDDLE = 0b0001111000
        RIGHT = 0b0111100000
        for mask in rows.values():
            left = (mask & LEFT) == 0
            middle = (mask & MIDDLE) == 0
            right = (mask & RIGHT) == 0
            if left and right:
                continue
            elif left or middle or right:
                ans -= 1
            else:
                ans -= 2
        return ans