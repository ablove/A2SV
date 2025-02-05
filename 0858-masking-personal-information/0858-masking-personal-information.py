class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:  
            s = s.lower()
            name, domain = s.split('@')
            return name[0] + "*****" + name[-1] + "@" + domain
        
        else: 
            digits = ''.join([ch for ch in s if ch.isdigit()])  
            local_number = "***-***-" + digits[-4:] 
            
            country_code_length = len(digits) - 10 
            if country_code_length == 0:
                return local_number
            else:
                return "+" + "*" * country_code_length + "-" + local_number

            













        