class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans=[0]*len(score)
        for i in range(len(score)):
            p=max(score)
            position=score.index(p)
            score[position]=-1
            if i==0:
                ans[position]='Gold Medal'
            elif i==1:
                ans[position]='Silver Medal'
            elif i==2:
                ans[position]='Bronze Medal'
            else:
                ans[position]=str(i+1)
        return ans
