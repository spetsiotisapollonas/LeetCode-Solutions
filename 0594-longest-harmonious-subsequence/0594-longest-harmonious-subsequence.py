class Solution:
    def findLHS(self, nums: List[int]) -> int:
        my_dict={}
        my_set=set(nums)
        best=0
        for num in nums:
            my_dict[num]=my_dict.get(num,0)+1
        for num in my_set:
            if num+1 in my_dict:
                ans=my_dict[num]+my_dict[num+1]
                best=max(best,ans)
            if num-1 in my_dict:
                ans=my_dict[num]+my_dict[num-1]
                best=max(best,ans)
        return best

