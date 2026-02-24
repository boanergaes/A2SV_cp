class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        ref = skill[0] + skill[-1]
        tot_chem = skill[0] * skill[-1]
        j = n - 2
        for i in range(1, n // 2):
            if skill[i] + skill[j] != ref:
                return -1
            tot_chem += skill[i] * skill[j]
            j -= 1
        return tot_chem