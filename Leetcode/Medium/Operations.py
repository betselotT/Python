class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        arr = []
        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if boxes[i] == '1' and boxes[j] == '1':
                    count += abs(j - i)
                elif boxes[i] == '0' and boxes[j] == '1':
                    count += abs(j - i)
            arr.append(count)
        return arr