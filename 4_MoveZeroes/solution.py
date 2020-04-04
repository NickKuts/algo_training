class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_cnt = 0
        
        for i in range(len(nums)):
            cur_elem = nums[i]
            
            if cur_elem != 0:
                nums[non_zero_cnt] = cur_elem
                non_zero_cnt += 1
        
        for i in range(non_zero_cnt, len(nums)):
            nums[i] = 0
        
        return nums
