class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = {}

        for num in nums:
            if num in checker:
                return True
            checker[num] = True

        return False
            