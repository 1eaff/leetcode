class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        base = 0
        ret = []
        for ix in range(len(nums)):
            if nums[ix] < 0: base = ix
        left, right = base, base + 1
        while left != -1 and right != len(nums):
            if abs(nums[left]) < abs(nums[right]):
                ret.append(nums[left] ** 2)
                left -= 1
            else:
                ret.append(nums[right] ** 2)
                right += 1
        while left != -1:
            ret.append(nums[left] ** 2)
            left -= 1
        while right != len(nums):
            ret.append(nums[right] ** 2)
            right += 1
        return ret

