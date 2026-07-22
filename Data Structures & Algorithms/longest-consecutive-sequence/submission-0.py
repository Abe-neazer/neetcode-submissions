class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        counter = 1
        final = 1

        for i in range(1, len(nums)):
            
            if nums[i] == nums[i - 1]:
                continue

            
            if nums[i] == nums[i - 1] + 1:
                counter += 1
            else:
                counter = 1

            final = max(final, counter)

        return final