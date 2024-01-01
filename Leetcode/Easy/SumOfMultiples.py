class Solution:
    def sumOfMultiples(self, n: int) -> int:
        counter = 0
        for number in range(1,n+1):
            if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
                counter += number
        return counter