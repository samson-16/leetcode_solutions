class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves =0
        while target >1:
            if maxDoubles >0:
                if target %2 ==0:
                    target = target //2
                    moves +=1
                    maxDoubles-=1
                else:
                    target -=1
                    moves +=1
            else:
                moves += target-1
                break
        return moves




        