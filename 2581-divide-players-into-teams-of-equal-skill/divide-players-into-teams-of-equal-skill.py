class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = 0
        skill.sort()
        l, r = 0, len(skill)
        chemistery = skill[0] + skill[-1]
        while l < r:
            if skill[l] + skill[r-1] == chemistery:
                res += skill[l] * skill[r-1]
            else:
                return -1
            l += 1
            r -= 1
        
        return res



        

        