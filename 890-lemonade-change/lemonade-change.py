class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # bills.sort()
        count  = {
            5:0,
            10:0,
            20:0
        }
     
        for i in range(len(bills)):
            if bills[i] ==5:
                count[5] +=1
            elif bills[i] ==10:
                if count[5] >0:
                    count[5]-=1
                    count[10] +=1
                else:
                    return False
            else:
                if count[10] >0 and count[5]>0:
                    count[10] -=1
                    count[5]-=1
                elif count[5] >=3:
                    count[5]-=3
                else:
                    return False
        return True


        