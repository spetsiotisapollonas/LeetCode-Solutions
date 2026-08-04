class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)<3:
            return 0
        left=0
        good=0
        my_set=set()
        for right in range(len(s)):
            while s[right] in my_set:
                my_set.remove(s[left])
                left+=1
            my_set.add(s[right])
            if len(my_set)==3:
                good+=1
                my_set.remove(s[left])
                left+=1
        return good