class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        arr = []
        seats.sort()
        students.sort()
        j = 0
        for i in range(len(seats)):
            arr.append(abs(seats[i] - students[j]))
            j += 1
        return sum(arr)