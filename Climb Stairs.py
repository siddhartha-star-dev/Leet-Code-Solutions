class Solution:
    def climbStairs(self, n: int) -> int:
        n1=1
        n2=0
        for i in range(n):
            n1,n2 = n1+n2,n1
        return n1
