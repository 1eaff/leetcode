class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cached = 0
        ret = []
        for n in nums:
            cached += n
            ret.append(cached)
        return ret