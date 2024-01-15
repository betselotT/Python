class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        left = 0
        right = 0
        curr_stack = []
        main_stack = []
        for i in s:
            if i == "(":
                left+=1
                curr_stack.append("(")
            else:
                right+=1
                curr_stack.append(")")
            if left==right:
                main_stack.extend(curr_stack[1:-1])
                curr_stack = []
        return "".join(main_stack)