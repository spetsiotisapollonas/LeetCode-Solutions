class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_len=0
        ans=''
        for i in range(len(s)):
            left=i
            right=i
            while left>=0 and right<len(s) and s[left]==s[right]:
                if right-left+1>best_len:
                    best_len=right-left+1
                    ans=s[left:right+1]
                left-=1
                right+=1
            left=i
            right=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                if right-left+1>best_len:
                    best_len=right-left+1
                    ans=s[left:right+1]
                left-=1
                right+=1
        return ans

                