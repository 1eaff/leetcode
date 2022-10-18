class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        prev = arr[0]; j = 1; n = len(arr)
        while j != n:
            if arr[j] > prev:
                prev = arr[j]; j += 1
            else:
                break
        if j == n: return False
        if j == 1: return False
        while j != n:
            if arr[j] < prev:
                prev = arr[j]; j += 1
            else:
                return False
        return True