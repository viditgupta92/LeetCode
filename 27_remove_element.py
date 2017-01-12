class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ctr = 0
        l = len(nums)
        for i in range(l):
            if i == l - ctr:
                break
            if nums[i] == val:
                flag = 0
                ctr += 1
                for j in range(i, l - 1, 1):
                    nums[j] = nums[j + 1]
                    flag = 1
                if flag == 1:
                    nums[j + 1] = val
        return len(nums)-ctr

s = Solution()
print(s.removeElement([4,5],4))