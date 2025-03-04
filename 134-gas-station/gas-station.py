class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total = 0 
        tank = 0   
        start = 0  
        
        for i in range(n):
            delta = gas[i] - cost[i]
            total += delta
            tank += delta
          
            if tank < 0:
                start = i + 1
                tank = 0
        
    
        return start if total >= 0 else -1
            