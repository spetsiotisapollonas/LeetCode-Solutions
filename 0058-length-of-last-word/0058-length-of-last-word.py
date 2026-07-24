class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip().split()
        ans=len(s[-1])
        return ans