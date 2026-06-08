class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        x = 1
        highest = 1
        if len(nums) == 0:
            return 0
        for actual_num, next_num in zip(sorted_nums, sorted_nums[1:]):
            if actual_num + 1 != next_num:
                if x > highest:
                    highest = x
                x = 1
            else:
                x += 1
                if highest < x:
                    highest = x
        return highest
            
                    


                

        