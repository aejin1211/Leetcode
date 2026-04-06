class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # k > 1 
        # numbers all positive, all negative
        n = len(nums)

        def next_index(index):
            return (index + nums[index]) % n

        def valid(num, direction):
            return (num > 0) == direction

        for i in range(n):
            slow = i
            fast = i

            direction = nums[i] > 0
            # True: positive, False: negative

            while True:
                slow = next_index(slow)
                fast = next_index(fast)

                if not valid(nums[slow], direction):
                    break

                if not valid(nums[fast], direction):
                    break
                
                fast = next_index(fast)
                if not valid(nums[fast], direction):
                    break

                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True
        return False