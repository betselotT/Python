class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_cities = set()
        end_cities = set()
        for i in paths:
            start_cities.add(i[0])
            end_cities.add(i[1])
        for i in end_cities:
            if i not in start_cities:
                return i