def answer(minions):
    # your code heredef answer(minions):
    A = len(minions)
    outList = []  
 
    #Algorithm: 
    #1. insert the first minion in the final list
    #2. Imple. insertion order algorithm, with score comparison
    outList.append(0)
    for i in range(1,A):
        for indxJ in range(len(outList)):
            #check weather i < j or not
            #if (minions[i][0] * minions[i][2] * minions[j][2]) < (minions[j][0] *( minions[i][1] * minions[j][2] - minions[i][2] * minions[j][1])):
            j = outList[indxJ] 
            scoreI = (float)(minions[i][0]) + (1 - (float)(minions[i][1])/minions[i][2])* (float)(minions[j][0])
            scoreJ = (float)(minions[j][0]) + (1 - (float)(minions[j][1])/minions[j][2])* (float)(minions[i][0])
            if scoreI < scoreJ:
                outList.insert(indxJ,i)
                break
            elif j == outList[len(outList)-1]:
                outList.append(i)
                break
            
            
            
        
        
    return outList
    
minions = [[5, 1, 5], [10, 1, 5], [23,1,3],[50,1,3],[23,1,3],[23,23,33],[23,23,33]]
#minions = [[5, 1, 5], [10, 1, 2]]
#minions = [[390, 185, 624], [686, 351, 947]]
#minions = [[5, 1, 5], [5, 1, 5],[5, 1, 5], [5, 1, 5],[5, 1, 5], [5, 1, 5]]
answer(minions)