class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        arr = []

        for i in range(length):
            for j in range(length-1,-1,-1):
                arr.append(matrix[j][i])


        k = 0
        for i in range(length):
            for j in range(length):
                matrix[i][j] = arr[k]
                k+=1