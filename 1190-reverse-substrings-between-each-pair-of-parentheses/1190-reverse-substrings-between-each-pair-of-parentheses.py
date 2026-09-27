class Solution(object):
    def reverseParentheses(self, s):
        stack = []

        for ch in s:
            if ch != ")":
                stack.append(ch)

            else:
                temp = ""

                while stack[-1] != "(":
                    temp += stack.pop()

                stack.pop()   # remove "("

                for c in temp:
                    stack.append(c)

        result = ""

        while stack:
            result += stack.pop()

        return result[::-1]