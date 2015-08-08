class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        total = 0
        while n != 0:
            total += n & 1
            n>>=1
        return total
