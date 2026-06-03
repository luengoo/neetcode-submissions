class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        normal_dict = {}
        for num in nums:
            key = num
            if key not in normal_dict:
                normal_dict[key] = 1
            else:
                normal_dict[key] += 1
        x = 0
        result = []
        while x is not k:
            removal = max(normal_dict, key=normal_dict.get)
            result.append(removal)
            normal_dict[removal] = -1
            x += 1
        return result