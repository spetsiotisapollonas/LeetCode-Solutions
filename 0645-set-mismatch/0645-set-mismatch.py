class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        my_sum1=0
        my_sum2=0
        d=0
        ans=[]
        for i in range(len(nums)):
            if i<len(nums)-1 and nums[i]==nums[i+1]:
                d=nums[i]
            my_sum1+=nums[i]
            my_sum2+=i+1
        my_sum1-=d
        ap=my_sum2-my_sum1
        ans.extend([d,ap])
        return ans
        