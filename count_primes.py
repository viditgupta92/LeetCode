class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ctr = 0
        for i in range(2, n, 1):
            flag = 1
            for j in range(i - 1, 1, -1):
                if i % j == 0:
                    flag = 0
            if flag == 1:
                ctr += 1
        return ctr

s = Solution()
print(s.countPrimes(49900))