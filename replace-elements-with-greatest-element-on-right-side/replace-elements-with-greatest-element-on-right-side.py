class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            arr[0] = -1; return arr
        m = arr[len(arr) - 1]
        i = len(arr) - 2
        while i != -1:
            tmp = arr[i]
            arr[i] = m
            m = tmp if tmp > m else m
            i -= 1
        arr[len(arr) - 1] = -1
        return arr