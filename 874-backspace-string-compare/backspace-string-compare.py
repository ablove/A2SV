class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for i in s:
            if i != "#":
                stack_s.append(i)
            elif i == "#" and stack_s:
                stack_s.pop()
            else:
                continue    
        for i in t:
            if i != "#":
                stack_t.append(i)
            elif i == "#" and stack_t:
                stack_t.pop()
            else:
                continue

        t1 = "".join(stack_t)
        s1 = "".join(stack_s)  

        return s1 == t1

        