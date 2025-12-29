class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()
        i = 0
        j = len(skill) - 1
        chemistry = 0
        sum = skill[0] + skill[len(skill)-1] 

        while i < j:
            if skill[i] + skill[j] != sum:
                return -1
            else:
                chemistry += skill[i] * skill[j]
                i += 1
                j -= 1

        return chemistry
