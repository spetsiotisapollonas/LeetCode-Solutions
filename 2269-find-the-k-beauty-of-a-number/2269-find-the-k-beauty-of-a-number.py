class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        k_beauty=0
        number=num
        num=str(num)
        left=0
        for right in range(k,len(num)+1):
            x=int(num[left:right])
            if x!=0 and number%x==0:
                k_beauty+=1
            left+=1
        return k_beauty