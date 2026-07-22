class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length_min=min(strs,key=len)
        ans=''
        for i in range(len(length_min)):
            check=set()
            for word in strs:
                check.add(word[i])
                w=word[i]
            if len(check)==1:
                ans+=w
            else:
                break
        return ans
                
        