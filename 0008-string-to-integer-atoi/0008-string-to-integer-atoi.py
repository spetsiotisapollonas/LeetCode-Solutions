class Solution:
    def myAtoi(self, s: str) -> int:
        ans=''
        for i in range(len(s)):
            if s[i]==' ':
                continue
            elif s[i]=='-' or s[i]=='+' or s[i].isdigit():
                if s[i]=='-':
                    prosimo=-1
                elif s[i]=='+':
                    prosimo=1
                else:
                    ans+=s[i]
                    prosimo=1
                k=i+1
                while k<len(s)and s[k].isdigit():
                    ans+=s[k]
                    k+=1
                break
            else:
                return 0
        if not ans:
            return 0
        ans=int(ans)*prosimo
        if ans<-(2**31):
            return -(2**31)
        elif ans>2**31-1:
            return 2**31-1
        return ans  
            
                    
                