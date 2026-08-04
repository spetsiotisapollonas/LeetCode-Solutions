class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if len(blocks)<k:
            return -1
        changes=0
        best=float('inf')
        for i in range(k):
            if blocks[i]=='W':
                changes+=1
        best=min(best,changes)
        left=0
        for right in range(k,len(blocks)):
            if blocks[right]=='W':
                changes+=1
            if blocks[left]=='W':
                changes-=1
            left+=1
            best=min(best,changes)
        return best
        
