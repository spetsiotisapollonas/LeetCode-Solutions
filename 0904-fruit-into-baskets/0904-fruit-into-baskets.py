class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        my_dict={}
        left=0
        best=0
        for right in range(len(fruits)):
            my_dict[fruits[right]]=my_dict.get(fruits[right],0)+1
            while len(my_dict)>2:
                my_dict[fruits[left]]-=1
                if my_dict[fruits[left]]==0:
                    del my_dict[fruits[left]]
                left+=1
            best=max(best,right-left+1)
        return best