class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1

        res = 0
        flag = 0
        for k, v in dic.items():
            if v % 2 == 0:
                res += v
            else:
                flag = 1
                res += v - 1
        if flag == 1:
            res += 1
        return res

s = Solution()
print(s.longestPalindrome("abccccdd"))