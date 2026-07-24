class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]=digits[-1]+1
        k=-1
        while digits[k]>9 and abs(k)<len(digits):
            digits[k]=0
            k=k-1
            digits[k]=digits[k]+1
        while digits[k]==10:
            digits[k]=0
            digits=[1]+digits
            k=k+1
        return digits