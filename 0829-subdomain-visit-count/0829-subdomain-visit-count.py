class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_count = defaultdict(int)

        for entry in cpdomains:
            count, domain = entry.split(" ")
            count = int(count)
            
            subdomains = domain.split(".")
            
            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                visit_count[subdomain] += count
        
        result = [f"{count} {domain}" for domain, count in visit_count.items()]
        return result
