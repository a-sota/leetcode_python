from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits == [9]:
            return [1,0]
        elif digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            return self.plusOne(digits[:len(digits)-1] + [0])


def test():
    s = Solution()
    assert s.plusOne([1,2,3]) ==  [1,2,4]
    print("OK")


if __name__ == "__main__":
    test()