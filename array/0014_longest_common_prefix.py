from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key = len)

        for i,ch in enumerate(shortest):
            for s in strs:
                if ch != s[i]:
                    return shortest[:i]
        return shortest  == "a"  


def test():
    s = Solution()
    assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert s.longestCommonPrefix(["dog","racecar","car"]) == ""
    print("OK")


if __name__ == "__main__":
    test()