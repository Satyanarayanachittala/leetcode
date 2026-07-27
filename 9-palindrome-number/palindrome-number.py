class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev =0
        temp=x
        while x>0:
            l=x%10
            rev = (rev*10)+l
            x=x//10
        if temp==rev:
            return True
        else :
            return False