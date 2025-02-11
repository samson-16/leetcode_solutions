class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        target = len(arr)
        # n = len(arr)
        ans =[]
        while target >0:
            max_found= arr.index(target)
            # swap
            # arr[0], arr[max_found] = arr[max_found], arr[0]
            if max_found !=0:
                arr[:max_found+1] = reversed(arr[:max_found+1])
                ans.append(max_found+1)
            #arr= list(reversed(arr[:max_found+1])) + arr[max_found+1:]
            #arr= list(reversed(arr[:target+1]))+ arr[target+1:]
            arr[:target] = reversed(arr[:target])
            # ans.append(max_found)
            ans.append(target)
            target-=1
            # n-=1
        return ans
        





        




    



        