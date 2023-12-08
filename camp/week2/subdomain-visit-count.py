class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for line in cpdomains:
            count, firstDomain = line.split()
            domains =[firstDomain]

            firstDot = (firstDomain.find('.'))+1
            if firstDot !=0:
                domains.append(firstDomain[firstDot:])
                secondDot = domains[1].find('.')+1
                if secondDot != 0:
                    domains.append(domains[1][secondDot:])
            for domain in domains:
                dic[domain] = dic.get(domain, 0)+int(count)
        res = []
        for key in dic:
            string = str(dic[key])+" "+key
            res.append(string)


        return res