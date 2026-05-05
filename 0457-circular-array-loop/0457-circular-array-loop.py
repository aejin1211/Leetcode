class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # same direction 
        # k > 1 
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        def valid(direction, i):
            return (nums[i] > 0) == direction


        for i in range(n):

            direction = nums[i] > 0
            slow = i
            fast = i

            while True:
                slow_next = next_index(slow)
                fast_next = next_index(fast)

                if not valid(direction, slow_next):
                    break
                if not valid(direction, fast_next):
                    break
                
                fast_next2 = next_index(fast_next)
                if not valid(direction, fast_next2):
                    break
                
                slow = slow_next
                fast = fast_next2
            
                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True
        return False    
            # curr = i
            # while valid(direction, curr):
            #     nxt = next_index(curr)
            #     nums[curr] = 0
            #     curr = nxt
            

