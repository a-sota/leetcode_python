from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)
        while l < r:
            mid = (l + r)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
        


def test():
    s = Solution()
    assert s.searchInsert([1,3,5,6],5) == 2
    assert s.searchInsert([1,3,5,6],2) == 1
    print("OK")


if __name__ == "__main__":
    test()