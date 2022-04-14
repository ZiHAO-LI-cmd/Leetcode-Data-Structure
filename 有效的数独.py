class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row = [[0]*10]*9
        # col = [[0]*10]*9
        # box = [[0]*10]*9
        # [array] * 3操作中，只是创建3个指向array的引用，所以一旦array改变，matrix中3个list也会随之改变。
        # https://blog.csdn.net/cxj540947672/article/details/85257589

        row = [[0] * 10 for _ in range(9)]
        col = [[0] * 10 for _ in range(9)]
        box = [[0] * 10 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                curNum = int(board[i][j])
                if row[i][curNum]:
                    return False
                if col[j][curNum]:
                    return False
                if box[int(j//3 + (i//3)*3)][curNum]:
                    return False
                
                # 之前都没出现过
                row[i][curNum] = 1
                col[j][curNum] = 1
                box[int(j//3 + (i//3)*3)][curNum] = 1

        return True
