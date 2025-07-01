# Last updated: 7/1/2025, 11:11:03 PM
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "]":
                chars = []
                while stack and stack[-1] != "[":
                    chars.append(stack.pop())
                chars.reverse()
                chars = "".join(chars)
                stack.pop() # get rid of the opening bracket
                
                count = []
                while stack and stack[-1].isnumeric():
                    count.append(stack.pop())
                count.reverse()
                count = int("".join(count))

                stack.append(chars * count)
            else:
                stack.append(s[i])
        return "".join(stack)


            
            
