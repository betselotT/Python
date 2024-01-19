class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        arr = []
        for i in range(len(image)):
            image[i].reverse()
            arr.append(image[i])
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                elif arr[i][j] == 1:
                    arr[i][j] = 0
        return arr