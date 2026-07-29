class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        pol=1
        ans=0
        left=0
        if k<=1:
            return 0
        for right in range(len(nums)):
            pol=pol*nums[right]
            while pol>=k:
                pol=pol/nums[left]
                left+=1
            ans+=(right-left+1)
        return ans