class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = defaultdict(int)
        total =0
        for i in range(len(answers)):
            rabbits[answers[i]] += 1

            if answers[i]+1 <rabbits[answers[i]]:
                total +=answers[i]+1
                rabbits[answers[i]]=1
        # print(total)
        for key in rabbits:
           
            total += key+1
        return total



        