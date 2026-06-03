class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = 0
        while x < len(nums):
            y = 1
            while x + y < len(nums):
                if nums[x] + nums[x + y] == target:
                    result = [x, x + y]
                    return result
                else:
                    y += 1
            x += 1

        result = [x, y]

