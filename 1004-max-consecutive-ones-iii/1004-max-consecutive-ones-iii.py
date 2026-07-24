class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        counts=0
        left=0
        best=0
        for right in range(len(nums)):
            if nums[right]==0:
                counts+=1
            while counts>k:
                if nums[left]==0:
                    counts-=1
                left+=1
            best=max(best,right-left+1)
        return best
