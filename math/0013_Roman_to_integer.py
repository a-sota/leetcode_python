from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        for c in reversed(s):
            if ans >= mp[c] * 5:
                ans -= mp[c]
            else:
                ans += mp[c]
        return ans



def test():
    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
    print("OK")


if __name__ == "__main__":
    test()