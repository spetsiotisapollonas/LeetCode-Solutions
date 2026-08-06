class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort()
        ans=[0]*k
        best=[]
        position=-1
        for i in range(k):
            ans[i]=arr[i]
            best.append(abs(arr[i]-x))
        for i in range(k,len(arr)):
            if abs(arr[i]-x)<max(best):
                position=best.index(max(best))
                best[position]=abs(arr[i]-x)
                ans[position]=arr[i]
        ans.sort()
        return ans

    