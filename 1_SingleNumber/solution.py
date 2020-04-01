class Solution:    
    def singleNumber(self, nums: List[int]) -> int:
        met_elements = dict()
        
        for num in nums:
            if num not in met_elements:
                met_elements[num] = 1
            else:
                met_elements[num] += 1
                
        for k, v in met_elements.items():
            if v == 1:
                return k
            
