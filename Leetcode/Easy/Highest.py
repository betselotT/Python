class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = []
        sum = 0
        for i in range(len(gain)):
            sum += gain[i]
            arr.append(sum)
        if max(arr) < 0:
            return 0
        else:
            return max(arr)