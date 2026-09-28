# Given an m x n matrix, return all elements of the matrix in spiral order.
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        rows, columns = len(matrix) , len(matrix[0])
        i = 0
        while i < len(matrix):
            print(i)
            res += matrix[ i ][0+i:len(matrix[0])-i]  + matrix[i+1:len(matrix)-i-1][-1] + matrix[len(matrix[-1])-i][-i-1:0+i] + matrix[len(matrix)-i-1:1+i][0]
            i+= 1
        return res


a = Solution()
print(a.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))