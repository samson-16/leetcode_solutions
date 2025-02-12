class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # costs.sort()
        cur = [0] * (max(costs)+1)

        for cost in costs:
            cur[cost]+=1
        target =0
        for index, val in enumerate(cur):
            for _ in range(val):
                costs[target] = index
                target +=1
        count =0
        print(costs)
        for cost in costs:
            if cost<=coins:
                coins-=cost
                count+=1
        return count


        