class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        n = len(nums)
        while i != n:
            if nums[i] == 0:
                i += 1
            else:
                nums[j] = nums[i]
                i += 1; j += 1
        while j != n:
            nums[j] = 0
            j += 1
        