class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        result = [[0] * len(row) for row in triangle]
        result[0][0] = triangle[0][0]
        for rowIndex, row in enumerate(triangle):
            if rowIndex == 0:
                continue
            else:
                for colIndex, col in enumerate(row):
                    if colIndex == 0:
                        minValue = result[rowIndex - 1][0]
                    elif colIndex == len(row) - 1:
                        minValue = result[rowIndex - 1][-1]
                    else:
                        minValue = min(result[rowIndex - 1][colIndex - 1],
                                       result[rowIndex - 1][colIndex])
                    result[rowIndex][colIndex] = col + minValue
        return min(result[-1])