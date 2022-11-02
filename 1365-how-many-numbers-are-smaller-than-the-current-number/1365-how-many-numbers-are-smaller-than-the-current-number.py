class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        m = [0] * 101
        ret = [0] * len(nums)
        for n in nums:
            m[n] += 1
        for ix in range(len(nums)):
            ret[ix] = sum(m[0:nums[ix]])
        return ret