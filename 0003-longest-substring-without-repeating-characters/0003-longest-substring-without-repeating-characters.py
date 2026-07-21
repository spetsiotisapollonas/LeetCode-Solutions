class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best=0
        characters=set()
        write=0
        for read in range(len(s)):
            while s[read] in characters:
               characters.remove(s[write])
               write+=1
            characters.add(s[read]) 
            best=max(best,read-write+1)
        return best