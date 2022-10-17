class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        lst = []
        for n in arr:
            if n == 0:
                lst.append(0); lst.append(0)
            else:
                lst.append(n)
        for ix in range(len(arr)):
            arr[ix] = lst[ix]