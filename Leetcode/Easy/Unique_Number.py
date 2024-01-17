class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        newArr = {}
        count = 0
        for i in range(len(arr)):
            count = arr.count(arr[i])
            newArr[arr[i]] = count
        ans = [x for x in newArr.values()]
        return len(ans) == len(set(ans))