class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best=float('inf')
        left=0
        the_sum=0
        for right in range(len(nums)):
            the_sum+=nums[right]
            while the_sum>=target:
                best=min(best,right-left+1)
                the_sum-=nums[left]
                left+=1
        if best==float('inf'):
            return 0
        return best