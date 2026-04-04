class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(curr):
            return (curr + nums[curr]) % n

        def valid(num, direction):
            return (num > 0) == direction
                

        for i in range(n):
            slow = i
            fast = i
            direction = nums[i] > 0
            #Positive: True, Negatvie: False
        
            while True:
                slow_next = next_index(slow)
                fast_next = next_index(fast)

                if not valid(nums[slow_next], direction):
                    break
                if not valid(nums[fast_next], direction):
                    break
                
                fast_next = next_index(fast_next)
                if not valid(nums[fast_next], direction):
                    break
                
                slow = slow_next
                fast = fast_next

                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True

        return False

        