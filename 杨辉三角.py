class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows + 1):
            res.append([1] * i)

        if numRows < 2:
            return res

        for j in range(2, numRows):
            for k in range(1, j):
                res[j][k] = res[j-1][k-1] + res[j-1][k]
        return res
