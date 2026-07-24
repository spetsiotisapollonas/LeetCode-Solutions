class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        low=0
        high=(m*n)-1
        while low<=high:
            mid=(high+low)//2
            p1=mid//n
            p2=mid%n
            if matrix[p1][p2]==target:
                return True
            elif matrix[p1][p2]>target:
                high=mid-1
            else:
                low=mid+1
        return False