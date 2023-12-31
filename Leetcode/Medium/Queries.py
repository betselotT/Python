class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = []
        answer = []
        for i in range(1, m + 1):
            arr.append(i)
        for query in queries:
            position = arr.index(query)
            answer.append(position)
            element = arr.pop(position)
            arr.insert(0, element)
        return answer