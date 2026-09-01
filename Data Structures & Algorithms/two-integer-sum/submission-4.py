class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prev = {}

        for i in range(len(nums)):
            prev[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prev and prev[diff] != i:

                return [i,prev[diff]]



        



        

 
        