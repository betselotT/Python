class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = list(range(1, m + 1))
        answer = []
        for query in queries:
            position = arr.index(query)
            answer.append(position)
            element = arr.pop(position)
            arr.insert(0, element)
        return answer