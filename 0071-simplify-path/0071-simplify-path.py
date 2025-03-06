class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split('/')
        print(paths)

        for x in paths:
            if x == "." or x == '':
                continue
            elif x == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(x)
                     
        return "/" + ("/").join(stack)           
          

    


        