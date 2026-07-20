class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        group = {}

        for i in range(len(nums)):
            if nums[i] not in group:
                group[nums[i]] = 0
            group[nums[i]] += 1

        result = []
        for i in range(k):
            max_num = max(group, key=group.get)  # find key with highest count
            result.append(max_num)
            group.pop(max_num)  # remove it so next max() call finds the next highest

        return result