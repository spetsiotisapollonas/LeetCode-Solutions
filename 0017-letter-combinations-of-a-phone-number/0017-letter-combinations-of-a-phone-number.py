class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results=[]
        my_dict={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        if not digits:
            return []
        def backtrack(start_index,path):
            if len(digits)==len(path):
                results.append(''.join(path))
                return
            digit=int(digits[start_index])
            for letter in my_dict[digit]:
                path.append(letter)
                backtrack(start_index+1,path)
                path.pop()
        backtrack(0,[])
        return results