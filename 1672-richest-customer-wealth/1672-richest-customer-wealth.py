class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for i in accounts:
            acc = 0
            for j in i:
                acc += j
            if acc > richest:
                richest = acc
        return richest