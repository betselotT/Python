class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [''] * len(s)
        for i, n in zip(indices, s):
            arr[i] = n
        return "".join(arr)
