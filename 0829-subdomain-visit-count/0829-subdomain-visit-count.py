class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_count = defaultdict(int)

        for entry in cpdomains:
            # Split the entry into visit count and domain
            count, domain = entry.split(" ")
            count = int(count)
            
            # Split the domain into subdomains
            subdomains = domain.split(".")
            
            # Add visits for all subdomains
            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                visit_count[subdomain] += count
        
        # Prepare the result in the required format
        result = [f"{count} {domain}" for domain, count in visit_count.items()]
        return result
