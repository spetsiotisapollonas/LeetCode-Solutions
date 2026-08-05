class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        my_sum=sum(nums)
        my_sum2=0
        for i in range(1,len(nums)+1):
            my_sum2+=i
        return my_sum2-my_sum
            
