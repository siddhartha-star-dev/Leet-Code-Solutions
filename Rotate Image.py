class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        l=0
        r = len(matrix)-1
        
        while (l<r):
            top = l
            bottom = r
            for i in range(r-l):
                topleft = matrix[top][l+i]
                matrix[top][l+i] = matrix[r-i][top]
                matrix[r-i][top] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[l+i][bottom]
                matrix[l+i][bottom] = topleft
            l+=1
            r-=1
