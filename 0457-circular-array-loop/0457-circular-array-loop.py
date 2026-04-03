class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        def valid(i, direction):
            return nums[i] != 0 and (nums[i] > 0) == direction

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            slow = i
            fast = i

            while True:
                slow_next = next_index(slow)
                fast_next = next_index(fast)

                if not valid(slow_next, direction):
                    break
                if not valid(fast_next, direction):
                    break

                fast_next2 = next_index(fast_next)
                if not valid(fast_next2, direction):
                    break

                slow = slow_next
                fast = fast_next2

                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True

            curr = i
            while valid(curr, direction):
                nxt = next_index(curr)
                nums[curr] = 0
                curr = nxt

        return False