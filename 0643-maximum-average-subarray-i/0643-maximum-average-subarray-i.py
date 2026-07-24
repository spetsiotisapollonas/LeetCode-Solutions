class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        the_sum=sum(nums[:k])
        current_sum=the_sum
        for i in range(k,len(nums)):
            current_sum=current_sum-nums[i-k]+nums[i]
            the_sum=max(the_sum,current_sum)
        return the_sum/k