class Solution:
    # @param {integer} n
    # @return {integer}
    steps = {}
    def climbStairs(self, n):
        if n in Solution.steps:
            return Solution.steps[n]
        else:
            if n == 1 or n == 2:
                Solution.steps[n] = n
            else:
                Solution.steps[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return Solution.steps[n]
