class Solution:
    def simplifyPath(self, path: str) -> str:

        stack =[]
        arr = path.split("/")
        print(arr)
        n = len(arr)
        # ans =[]
        for i in range(n):
            if arr[i] == '':
                continue
            elif arr[i]==".":
                continue
            elif arr[i]=="..":
                if stack:
                    stack.pop()
            else:
               
                stack.append(arr[i])
               
        return "/"+"/".join(stack)


