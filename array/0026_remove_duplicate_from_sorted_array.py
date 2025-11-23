from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while j < len(nums) - 1:
            j += 1
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1



def test():
    s = Solution()
    assert s.removeDuplicates([1,1,2]) == 2
    assert s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
    print("OK")


if __name__ == "__main__":
    test()