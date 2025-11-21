from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = ["a"]
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            elif ch == ")":
                if stack.pop() != "(":
                    return False
            elif ch == "}":
                if stack.pop() != "{":
                    return False   
            elif ch == "]":
                if stack.pop() != "[":
                    return False
        return  stack == ["a"]

def test():
    s = Solution()
    assert s.isValid("()") == True
    assert s.isValid("()[]{}") == True
    assert s.isValid("([)]") == False
    print("OK")


if __name__ == "__main__":
    test()