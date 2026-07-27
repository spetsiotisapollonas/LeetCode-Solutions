class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        the_dict={}
        for num in nums:
            the_dict[num]=the_dict.get(num,0)+1
        ans=min(the_dict,key=the_dict.get)
        return ans