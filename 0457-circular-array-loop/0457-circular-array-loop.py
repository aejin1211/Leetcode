class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(curr):
            return (curr + nums[curr]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            slow = i
            fast = i

            while True:
                # slow 한 칸 이동 가능 여부 확인
                next_slow = next_index(slow)
                if nums[slow] == 0 or (nums[slow] > 0) != direction:
                    break
                if nums[next_slow] == 0 or (nums[next_slow] > 0) != direction:
                    break

                # fast 한 칸 이동 가능 여부 확인
                next_fast = next_index(fast)
                if nums[fast] == 0 or (nums[fast] > 0) != direction:
                    break
                if nums[next_fast] == 0 or (nums[next_fast] > 0) != direction:
                    break

                # 실제 이동
                slow = next_slow
                fast = next_index(next_fast)

                # fast 두 번째 이동 후도 방향 확인
                if nums[fast] == 0 or (nums[fast] > 0) != direction:
                    break

                if slow == fast:
                    # self-loop 방지
                    if slow == next_index(slow):
                        break
                    return True

            # 이번 시작점에서 지나간 경로는 0으로 마킹
            curr = i
            while nums[curr] != 0 and (nums[curr] > 0) == direction:
                nxt = next_index(curr)
                nums[curr] = 0
                curr = nxt

        return False
       