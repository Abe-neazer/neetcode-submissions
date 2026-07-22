class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        lenn = len(numbers)
        
        left = 0
        right = lenn -1

        i = 0 
        while i < lenn:

            if numbers[left] == numbers[right]:
                left += 1
                continue

            check = numbers[left] + numbers[right]
            if check == target:
                return [left+1, right+1]
            elif check > target:
                right -= 1
            else:
                left += 1

           
            i += 1 

        return []
