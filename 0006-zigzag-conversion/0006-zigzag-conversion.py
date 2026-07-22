class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        rows=['']*numRows
        line=0
        step=1
        for char in s:
            rows[line]+=char
            if line==0:
                step=1
            elif line==numRows-1:
                step=-1
            line+=step
        result=''.join(rows)
        return result
            



                

                



