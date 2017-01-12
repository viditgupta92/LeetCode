class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = bin(x)
        b = bin(y)
        res = bin(int(a,2) ^ int(b,2))
        ctr = 0
        for i in res[2:]:
            if i == '1':
                ctr += 1
        print(ctr)

s = Solution()
s.hammingDistance(1,4)