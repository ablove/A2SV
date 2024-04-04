class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums=[i for i in range(0,int(math.sqrt(c)+1))]
        l,r=0,len(nums)-1
        # if c==1:
        #     return True

        while l<=r:
            num=(l*l)+(r*r)
            if num == c:
                return True
            elif num>c:
                
                r -= 1
            else:
                l += 1    
        return False 










        