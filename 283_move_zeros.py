class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ctr = 0
        l = len(nums)
        start = l
        for i in range(l):
            if nums[i] == 0:
                ctr += 1
                for j in range(i,l-1,1):
                    nums[j] = nums[j+1]
            if i == l - ctr:
                start = l - ctr
                break
        for i in range(start,l,1):
            nums[i] = 0

s = Solution()
s.moveZeroes([1])