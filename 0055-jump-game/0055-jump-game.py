class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        jump_index = n-2
        goal = n-1
        
        # flag = True
        while jump_index >= 0:
            if nums[jump_index]  >= (goal - jump_index):
                goal = jump_index
            jump_index -= 1
    
        return not goal       







        












        