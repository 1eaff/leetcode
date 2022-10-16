class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        steps = 0
        while num != 0:
            steps += (2 if num & 1 == 1 else 1)
            num = num >> 1
        return steps - 1