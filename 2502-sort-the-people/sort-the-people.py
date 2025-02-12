class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people ={}

        for i in range(len(heights)):
            people[heights[i]] = names[i]
        people_sort = sorted(people.items(), key= lambda a: a[0], reverse= True)
        
        return [x[1] for x in people_sort]


        