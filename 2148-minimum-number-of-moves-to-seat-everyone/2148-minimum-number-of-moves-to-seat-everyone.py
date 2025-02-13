class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        seats.sort()
        students.sort()
        
        i, j = 0, 0 
        moves = 0

        while i < len(seats):
            moves += abs(seats[i] - students[j])
            i += 1
            j += 1

        return moves
        