from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = 0
        for ch in reversed(s):
            if i > 0 and ch == " ":
                return i
            if ch != " ":
                i += 1
        return i


def test():
    s = Solution()
    assert s.lengthOfLastWord("Hello World") == 5
    assert s.lengthOfLastWord("   fly me   to   the moon  ") == 4
    print("OK")


if __name__ == "__main__":
    test()