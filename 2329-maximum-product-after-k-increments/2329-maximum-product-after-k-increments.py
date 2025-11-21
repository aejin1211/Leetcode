class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        
        result = 1
        mod = 10 ** 9 + 7
        heapify(nums)

        for i in range(k):
            current_min = heapq.heappop(nums)
            current_min += 1
            heapq.heappush(nums, current_min)
        
        for num in nums:
            result = result * num

        return result % mod

            
        