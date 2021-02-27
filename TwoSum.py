class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        oldNum = {}
        for i in range(len(nums)):
            if oldNum.get(target-nums[i]) is not None:
                return [oldNum.get(target-nums[i]), i]
            else:
                oldNum[nums[i]] = i