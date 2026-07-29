class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums2=[x**2 for x in nums]
        nums2.sort()
        return nums2