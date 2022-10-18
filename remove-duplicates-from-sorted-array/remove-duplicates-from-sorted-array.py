class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        n = len(nums)
        p = nums[0] - 1
        while i != n:
            if p == nums[i]:
                i += 1
                continue
            else:
                nums[j] = nums[i]
                p = nums[i]
                i += 1; j += 1
        return j