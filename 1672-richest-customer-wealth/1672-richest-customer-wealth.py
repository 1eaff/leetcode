class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(_) for _ in accounts])