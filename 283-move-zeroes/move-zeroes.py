class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # for i in nums:
        #     if i==0:
        #         nums.remove(i)
        #         nums.append(i)
        # here is another approach

        placeholder=0
        for seeker in range(len(nums)):
            if nums[seeker]!= 0:
                nums[placeholder],nums[seeker]=nums[seeker],nums[placeholder]
                placeholder += 1
















                


            
        """
        Do not return anything, modify nums in-place instead.
        """
        

            

            

            
        


        