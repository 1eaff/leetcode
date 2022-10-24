class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        nums = []
        n = 0
        _ = x
        while _ != 0:
            nums.append(_ % 10)
            _ = _ // 10
            n += 1
        i, j = 0, n - 1
        while i < j:
            if nums[i] != nums[j]:
                return False
            else:
                i += 1; j -= 1;
        return True