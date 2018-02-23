def answer(minions):
    # your code here
    A = len(minions)
    outList =range(A)
    finalOutList = []
    inList = outList
    loopList = outList[:]
    outList = []  
    totalProbability = 0.0
    totalTime = 0.0
    
    
    #Algorithm: 
    #1. insert the first minion in the final list
    #2. calculate the estimated time for the whole list for every possible positions. 
    #3. insert it in the position with the lowest score.
    #3. remove it from the inlist
    #4. loop until inlist is empty
    
    for i in loopList:
        lowIndx = 0
        lowScore = 1024 * 50   #unf
        for j in range(len(outList)+1):
            outList.insert(j,i)
            #calculate the list score
            totalProbability = 0
            totalTime = 0
            for m in outList:
                totalTime +=(1- totalProbability)* (float)(minions[m][0])
                totalProbability += (float)(minions[m][1])/minions[m][2]
            #check for the lowest_score
            if (totalTime) <= (lowScore):  #<= not < to ensure lexi. order
                lowIndx = j
                lowScore = totalTime
            
            outList.remove(i)
        outList.insert(lowIndx,i)
        inList.remove(i)
            
            
        
        
    return outList