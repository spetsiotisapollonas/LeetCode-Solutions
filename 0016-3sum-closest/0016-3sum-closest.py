class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best=float('inf')
        nums.sort()
        ans=-1
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                if s-target==0:
                    return s
                elif s>target:
                    if abs(s-target)<best:
                        best=abs(s-target)
                        ans=s
                    right-=1
                else:
                    if abs(s-target)<best:
                        best=abs(s-target)
                        ans=s
                    left+=1
        return ans
                
                