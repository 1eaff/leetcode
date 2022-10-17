class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = cnt = 0
        for i in nums:
            if i == 1:
                cnt += 1
            else:
                m = cnt if cnt > m else m
                cnt = 0
        m = cnt if cnt > m else m
        return m
