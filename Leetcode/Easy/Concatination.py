class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newList = []
        for elements in nums:
            newList.append(elements)
        for elements in nums:
            newList.append(elements)
        return newList