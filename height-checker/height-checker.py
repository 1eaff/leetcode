class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted = heights[:]
        sorted.sort()
        cnt = 0
        for ix in range(len(heights)):
            if heights[ix] != sorted[ix]: cnt += 1
        return cnt