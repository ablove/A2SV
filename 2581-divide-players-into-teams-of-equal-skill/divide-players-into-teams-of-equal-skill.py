class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()
        l, r = 0, len(skill)-1
        chemistry = 0

        while l < r:

            summ = skill[l] + skill[r]
            summ1 = skill[l+1] + skill[r-1]
            
            if summ != summ1:
                return -1
                break
            else:
                chemistry = chemistry + (skill[l] * skill[r])
                l += 1
                r -= 1
        return chemistry    




























        # skill.sort()
        # l, r = 0, len(skill)-1
        # chemistry = 0

        # while l < r:
        #     summ = skill[l] + skill[r]
        #     summ1 = skill[l+1] + skill[r-1]
        #     if summ != summ1:
        #         return -1
        #         break
        #     else:
        #         chemistry = chemistry + (skill[l] * skill[r])
        #         l += 1
        #         r -= 1
        # return chemistry        




















        # res = 0
        # skill.sort()
        # l, r = 0, len(skill)
        # chemistery = skill[0] + skill[-1]
        # while l < r:
        #     if skill[l] + skill[r-1] == chemistery:
        #         res += skill[l] * skill[r-1]
        #     else:
        #         return -1
        #     l += 1
        #     r -= 1
        
        # return res



        

        