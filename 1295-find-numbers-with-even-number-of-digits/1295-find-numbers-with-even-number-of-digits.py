class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        has_even_digits = lambda n: (10 <= n <= 99) or (1000 <= n <= 9999)  or (n == 100000)
        cnt = 0
        for n in nums:
            if (has_even_digits(n)):
                cnt += 1
        return cnt