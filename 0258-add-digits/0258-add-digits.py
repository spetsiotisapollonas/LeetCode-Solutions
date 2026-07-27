class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            k=num%10
            num=num//10
            num=num+k
        return num