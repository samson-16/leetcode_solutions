# Last updated: 5/28/2025, 7:55:27 PM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in cars]

        fleets = 0
        prev_time = 0
        for time in times:
            if time > prev_time:
                fleets += 1
                prev_time = time  
        return fleets