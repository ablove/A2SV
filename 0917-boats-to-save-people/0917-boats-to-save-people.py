class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        left, right = 0, len(people)-1
        boat_count = 0

        while left <= right:
            summ = people[left] + people[right]

            if summ >limit:
                boat_count += 1
                right -= 1

            else:
                boat_count += 1
                left += 1
                right -= 1
        return boat_count            


        























    # # Sort the weights of people
    #     people.sort()
    #     left, right = 0, len(people) - 1
    #     boats = 0

    #     while left <= right:
    #     # If the lightest and heaviest person can share a boat
    #         if people[left] + people[right] <= limit:
    #             left += 1  # Move the left pointer inward
    #     # The heaviest person always gets a boat
    #         right -= 1
    #         boats += 1  # Increment boat count
    
    #     return boats





            

            

        



        