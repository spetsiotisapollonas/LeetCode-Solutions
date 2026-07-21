class Solution:
    def reverse(self, x: int) -> int:
        prosimo=1
        if x<0:
            prosimo=-1
        x=abs(x)
        x=str(x)
        x=int(x[::-1])*prosimo
        if x<-(2**31) or x>2**31-1:
            return 0
        return x

