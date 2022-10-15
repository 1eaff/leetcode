class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for ix in range(1, len(nums)):
            nums[ix] += nums[ix - 1]
        return nums