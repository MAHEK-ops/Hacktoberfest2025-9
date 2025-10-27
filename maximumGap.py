import math
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        
        gap = math.ceil((max_val - min_val) / (n - 1))
        min_bucket = [float('inf')] * (n - 1)
        max_bucket = [float('-inf')] * (n - 1)
        
        for num in nums:
            if num == min_val or num == max_val:
                continue
            index = (num - min_val) // gap
            min_bucket[index] = min(min_bucket[index], num)
            max_bucket[index] = max(max_bucket[index], num)
        
        max_gap = 0
        prev_max = min_val
        
        for i in range(n - 1):
            if min_bucket[i] == float('inf'):
                continue
            max_gap = max(max_gap, min_bucket[i] - prev_max)
            prev_max = max_bucket[i]
        
        max_gap = max(max_gap, max_val - prev_max)
        return max_gap
