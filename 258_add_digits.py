class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = num
        res = 0
        r = self.sum_digits(temp, res)
        while r >= 10:
            temp = r
            res = 0
            r = self.sum_digits(temp, res)
        return r

    def sum_digits(self, temp, res):
        while temp > 0:
            res += temp % 10
            temp = int(temp/10)
        return res

s = Solution()
print(s.addDigits(19))