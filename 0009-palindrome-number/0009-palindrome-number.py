class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x>2**31-1:
            return 2**31-1
        x=str(x)
        return x==x[::-1]
        