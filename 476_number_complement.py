class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = bin(num)
        n = str(n[2:])

        lst = [int(i) for i in str(n)]
        for i in range(len(lst)):
            if lst[i] == 1:
                lst[i] = '0'
            else:
                lst[i] = '1'
        j = 0
        while lst[j] == 0:
            lst = lst[j+1:]
        lst = "".join(lst)
        print(int(lst,2))






s = Solution()
s.findComplement(5)