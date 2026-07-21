class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers={}
        for i in range(len(nums)):
            up=target-nums[i]
            if up in numbers:
                pos=numbers[up]
                return [pos,i]
            numbers[nums[i]]=i
        return None