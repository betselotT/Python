class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        newList = []
        k = celsius + 273.15
        f = celsius * 1.80 + 32.00
        newList.append(k)
        newList.append(f)
        return newList