class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        the_set=set(nums)
        if len(the_set)==len(nums):
            return False
        return True