class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        left, right = 0, int(math.sqrt(c))+1
        
        flag = False
        while left<= right:
            summ = left**2 + right**2
            # print(left, right)
            if summ == c:
                flag = True
                break
            elif summ > c:
                right -= 1
            else:
                left += 1

        return flag            
                        


















        # nums=[i for i in range(0,int(math.sqrt(c)+1))]
        # l, r = 0, len(nums)-1

        # while l <= r:
        #     num = (l*l) + (r*r)
        #     if num == c:
        #         return True
        #         break

        #     elif num > c:   
        #         r -= 1
        #     else:
        #         l += 1
        # return False  



        
                






















        # nums=[i for i in range(0,int(math.sqrt(c)+1))]
        # l,r=0,len(nums)-1
        # # if c==1:
        # #     return True

        # while l<=r:
        #     num=(l*l)+(r*r)
        #     if num == c:
        #         return True
        #     elif num>c:
                
        #         r -= 1
        #     else:
        #         l += 1    
        # return False 



        










        