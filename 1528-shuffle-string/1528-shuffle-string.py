class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = len(s)
        arr = [0] * l
        for ix in range(l):
            arr[indices[ix]] = s[ix]
        return ''.join(arr)