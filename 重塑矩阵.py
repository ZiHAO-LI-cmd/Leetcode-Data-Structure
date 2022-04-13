class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        res = []
        tmp = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                tmp.append(mat[i][j])
        index = 0
        temp = []
        for k in range(r):
            for m in range(c):
                temp.append(tmp[index])
                index += 1
            res.append(temp)
            temp = []
        return res
                    

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        
        ans = [[0] * c for _ in range(r)]
        for x in range(m * n):
            ans[x // c][x % c] = nums[x // n][x % n]
        
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/reshape-the-matrix/solution/zhong-su-ju-zhen-by-leetcode-solution-gt0g/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。