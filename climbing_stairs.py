class Solution:
    def climbStairs(self, n: int) -> int:
        i, ii = 1, 1
        
        for j in range(n-1):
            tmp = i
            i += ii
            ii = tmp
        return i

