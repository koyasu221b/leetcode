class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if nums is None or len(nums) == 0:
            return nums
        output = []
        for i in range(len(nums)):
            if i == 0:
                cnt = nums[0]
                start = end = nums[i]
            else:
                cnt += 1
                if nums[i] == cnt:
                    end = nums[i]
                else:
                    if start!=end:
                        output.append("%d->%d" % (start, end))
                    else:
                        output.append("%d" % end)
                    start = end = nums[i]
                    cnt = nums[i]
        if start!=end:
            output.append("%d->%d" % (start, end))
        else:
            output.append("%d" % end)
        return output
