class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s2=''
        for i in s:
            if i.isalnum():
                s2+=i.lower()
        return s2==s2[::-1]