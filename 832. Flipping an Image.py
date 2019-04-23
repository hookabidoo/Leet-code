
 def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        flip =[]
        invert =[]
        for i in A:
            flip.append(i[::-1])
        for i in flip:
            print(i)
            for x in range(len(i)):
                
                if i[x] == 0:
                    i[x]=1
                    # print(i[x])
                else:
                    i[x]=0
                    # print(i[x])
            invert.append(i)
        return invert

class Solution:
    def flipAndInvertImage(self, A: 'List[List[int]]') -> 'List[List[int]]':
        return [[1-j for j in i[::-1]] for i in A]