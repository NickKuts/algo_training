class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Int means 32 bits
        partial_sum = 0
        max_sum_seen = - (2**31 - 1)
        
        for i in nums:
            partial_sum += i
            
            if partial_sum > max_sum_seen:
                max_sum_seen = partial_sum
            
            if partial_sum < 0:
                partial_sum = 0
    
        return max_sum_seen
