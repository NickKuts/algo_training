class Solution:
    def isHappy(self, n: int) -> bool:
        digits = [int(i) for i in str(n)]
        seen_answers = set()
        
        while True:
            current_sum = sum([i*i for i in digits])
            
            if current_sum == 1:
                return True
            elif current_sum in seen_answers:
                return False
            else:
                seen_answers.add(current_sum)
                
            digits = [int(i) for i in str(current_sum)]
