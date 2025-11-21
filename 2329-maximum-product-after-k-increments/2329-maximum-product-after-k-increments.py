class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        min_heap = []
        result = 1
        mod = 10 ** 9 + 7
        for num in nums:
            heapq.heappush(min_heap, num)

        for i in range(k):
            current_min = heapq.heappop(min_heap)
            current_min += 1
            heapq.heappush(min_heap, current_min)
        
        for num in min_heap:
            result = result * num

        return result % mod

            
        