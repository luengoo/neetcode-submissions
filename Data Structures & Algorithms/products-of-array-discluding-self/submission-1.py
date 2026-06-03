class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        list_len = len(nums)
        result = []
        while i < list_len:
            new_list = nums[:i] + nums[i + 1:]
            product = 1
            for num in new_list:
                product *= num
            result.append(product)
            i += 1
        return result
