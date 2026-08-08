class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict={}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                p1=my_dict[nums[i]]
                p2=i
                if p2-p1<=k:
                    return True
            my_dict[nums[i]]=i
        return False
