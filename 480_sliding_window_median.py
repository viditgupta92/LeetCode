class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        med = []
        l = len(nums)
        # for i in range(l - k + 1):
        #     res = []
        #     for j in range(i,i+k,1):
        #         res.append(nums[j])
        #     res = sorted(res)
        #     if k %2 == 0:
        #         temp = float((res[int(k/2)-1] + res[int(k/2)])/2)
        #     else:
        #         temp = float(res[int(k/2)])
        #     med.append(temp)
        # return med
        for i in range(l - k + 1):
            res = nums[i:(i+k)]
            res = sorted(res)
            if k %2 == 0:
                temp = (res[int(k/2)-1] + res[int(k/2)])/float(2)
            else:
                temp = float(res[int(k/2)])
            med.append(temp)
        return med

s = Solution()
#s.medianSlidingWindow([1,3,-1,-3,5,3,6,7],3)
s.medianSlidingWindow([1],1)