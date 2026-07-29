class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return self.k1(s,left+1,right) or self.k2(s,left,right-1)
            left+=1
            right-=1
        return True
    def k1(self,s,left,right):
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    def k2(self,s,left,right):
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True