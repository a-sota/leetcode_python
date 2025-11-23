from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        for i in range(h - n + 1):
            if haystack[i : i + n] == needle:
                return i
        return -1



def test():
    s = Solution()
    assert s.strStr("sadbutsad","sad") == 0
    assert s.strStr("leetcode","leeto") == -1
    print("OK")


if __name__ == "__main__":
    test()