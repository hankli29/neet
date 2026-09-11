class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        num_fleets = 0

        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort()

        for i in range(len(pairs) - 1, -1, -1):
            pos, sp = pairs[i]
            time_needed = (target - pos) / sp

            if not stack:
                stack.append(time_needed)
                num_fleets += 1
                continue

            if time_needed > stack[-1]:
                num_fleets += 1
                stack.append(time_needed)
        
        return num_fleets




