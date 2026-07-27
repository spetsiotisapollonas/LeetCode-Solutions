class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()
        left=0
        right=0
        while right<len(nums):
            if right-left<=k and nums[right] in window:
                return True
            elif right-left<=k:
                window.add(nums[right])
                right+=1
            else:
                window.remove(nums[left])
                left+=1
        return False
            