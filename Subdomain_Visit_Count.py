#leetcode

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        buff = {}

        for doms in cpdomains:
            dom = doms.split(' ')
            vis = int(dom[0])
            sd = dom[1].split('.')

            subs = []
            substr = ''
            for i in range(len(sd) - 1, -1, -1):
                substr = sd[i] + '.' + substr
                subs.append(substr[:len(substr) - 1])

            for sub in subs:
                buff[sub] = buff.get(sub, 0) + vis

        return [str(buff[k]) + " " + k for k in buff]
