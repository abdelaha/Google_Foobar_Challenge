import random
import copy

def answer1(subway):
    # The reason my first approach fail, because it try to find the meeting point and path
    # however we want only to know if the graph have it or not without finding it
    # my second attempt will try to do so
    
    # To do so, we need to understand the properties of the graph that can get this sol:
    # e.g: the meeting point has to be reachable by others
    #      with the same number of steps
    #      with the same sequence of lines
    
    # get first order reachability tree from subway
    
    #Variables, constants, ... etc initializations
    n = len(subway)     # number of stations (1 50)
    m = len(subway[0])  # number of lines (red, blue, ... etc) (1 <= m <= 5)
    rechableStation = []
  
    for i in range(0,n):
        rechableStation.append([])

    doneItr = True;
    
  
    # First reachability Iteration
    for i in range(0,n):
        for j in range(0,m):
            if rechableStation[subway[i][j]].count(i) == 0:   # to prevent redundance
                rechableStation[subway[i][j]].append(i)
            
    
    while(doneItr):  
        doneItr = False   # stoping condition
        for elm in  rechableStation:
            for station in elm:
                for dest in rechableStation[station]:
                    if elm.count(dest) == 0:
                        doneItr = True
                        elm.append(dest)
                    
    numReachablestatuion = [len(x) for x in rechableStation]
    
    if numReachablestatuion.count(n) > 0:
        return -1
    else:
        for j in range(0,n):
            rechableStationCopy = copy.deepcopy(rechableStation)
            closedRechStat = rechableStationCopy[j]
            if closedRechStat.count(j) > 0:
                for i in range(0,n):
                    if subway[i].count(j) and i != j and rechableStationCopy[i].count(j) == 0:
                         rechableStationCopy[i].append(i)
            rechableStationCopy.pop(j)
            doneItr = True
            while(doneItr):
                doneItr = False
                for elm in rechableStationCopy:
                    if elm.count(j) > 0:
                        elm.remove(j)
                        [elm.append(x) for x in closedRechStat]
                numReachablestatuion = [len(x) for x in rechableStationCopy]
                if numReachablestatuion.count(n-1) > 0:
                        return j
        return -2

def closeStation(subway,stationIdx):
    station = subway[stationIdx];
    
    for i in range(0,len(subway)):
        for j in range(0,len(station)):
            if subway[i][j] == stationIdx:
                if station[j] == stationIdx:
                    subway[i][j] = i
                else:
                    subway[i][j] = station[j]

    
    subway.pop(stationIdx)
    for e in range(0,len(subway)):
        for s in range(0,len(subway[e])):
            if subway[e][s] > stationIdx:
                subway[e][s] -= 1
    
    return subway
def hasMeetingPointOld(subway):
    # The reson my first apprach fail, becasue it try to find the meeting point and path
    # however we want only to know if the graph have it or not without finding it
    # my second attempt will try to do so
    
    # To do so, we need to understand the properity of the graph that can get this sol:
    # e.g: the meeting point has to be reachable by all stations
    #      with the same number of steps
    #      with the same sequence of lines  (non feasable, naive feature since this is the solution)
    
    # get first order reachability tree from subway
    
    #Variables, constants, ... etc initializations
    n = len(subway)     # number of stations (1 50)
    m = len(subway[0])  # number of lines (red, blue, ... etc) (1 <= m <= 5)
    rechableStation = []
   # numOfSteps = [[0]*n]*n
  
    for i in range(0,n):
        rechableStation.append([])

    doneItr = True;
    
  
    # First rechability Iteration
    for i in range(0,n):
        for j in range(0,m):
            if rechableStation[subway[i][j]].count(i) == 0:   # to prevent redundance
                rechableStation[subway[i][j]].append(i)
               # numOfSteps[subway[i][j]][i] = 1
            
    elementryReachable = copy.deepcopy(rechableStation)
    while(doneItr):  
        doneItr = False   # stoping condition
        for elm in  rechableStation:
            for station in elm:
                for dest in rechableStation[station]:
                    if elm.count(dest) == 0:
                        doneItr = True
                        elm.append(dest)
                        #numOfSteps[rechableStation.index(elm)][dest] = numOfSteps[station][dest] + 1
                    
    numReachablestatuion = [len(x) for x in rechableStation]
    
    sol = -2
    for i in range(0, n):
        if len(rechableStation[i]) == n:
            rechabilityPath = [elementryReachable[i]]
            if len(elementryReachable[i]) == n:
                sol = -1
                doneItr = False
            else:
                doneItr = True
            
            while(doneItr):
                newSet = []
                doneItr = False
                for e in rechabilityPath[len(rechabilityPath)-1]:
                    newSet += elementryReachable[e]
                newSet = list(set(newSet))
                if len(newSet) == n:
                    return -1
            
                if rechabilityPath.count(newSet) == 0:
                    doneItr = True  
                    rechabilityPath.append(newSet)
                    
            
            
    
    return sol
def hasMeetingPoint(subway):
    # The reson my first apprach fail, becasue it try to find the meeting point and path
    # however we want only to know if the graph have it or not without finding it
    # my second attempt will try to do so
    
    # To do so, we need to understand the properity of the graph that can get this sol:
    # e.g: the meeting point has to be reachable by others
    #      with the same number of steps
    #      with the same sequence of lines
    
    # get first order reachability tree from subway
    
    #Variables, constants, ... etc initializations
    n = len(subway)     # number of stations (1 50)
    m = len(subway[0])  # number of lines (red, blue, ... etc) (1 <= m <= 5)
    rechableStation = []
    elementryReachableFromLine = []
   # numOfSteps = [[0]*n]*n
  
    for i in range(0,n):
        rechableStation.append([])
        elementryReachableFromLine.append([])
        for j in range(0,m):
            elementryReachableFromLine[len(elementryReachableFromLine)-1].append([])

    doneItr = True;
    
  
    # First rechability Iteration
    for i in range(0,n):
        for j in range(0,m):
            if rechableStation[subway[i][j]].count(i) == 0:   # to prevent redundance
                rechableStation[subway[i][j]].append(i)
                elementryReachableFromLine[subway[i][j]][j].append(i)
               # numOfSteps[subway[i][j]][i] = 1
            
    elementryReachable = copy.deepcopy(rechableStation)
    while(doneItr):  
        doneItr = False   # stoping condition
        for elm in  rechableStation:
            for station in elm:
                for dest in rechableStation[station]:
                    if elm.count(dest) == 0:
                        doneItr = True
                        elm.append(dest)
                        #numOfSteps[rechableStation.index(elm)][dest] = numOfSteps[station][dest] + 1
                    
    #numReachablestatuion = [len(x) for x in rechableStation]
    sol = -2
    doneItr = True
    for i in range(0, n):
        if len(rechableStation[i]) == n:    # check only fully reachable stations
            rechabilityPath = []
            for e in  elementryReachableFromLine[i]:
                rechabilityPath.append([e])
                if len(e) == n:
                    sol = -1
                    doneItr = False
                    
            itrIdx = 1
            while(doneItr):
                newSet = [[] for i in range(0,m)]
                doneItr = False
                for line in range(0,m):
                    for station in rechabilityPath[line][itrIdx]:
                        newSet[line] += elementryReachableFromLine[station][line]
                    newSet[line] = list(set(newSet[line]))  #remove redundance
                    if len(newSet[line]) == n:
                        return -1
                    if rechabilityPath[line].count(newSet[line]) == 0:
                        doneItr = True  
                        rechabilityPath[line].append(newSet[line])
                    
                itrIdx += 1
            
    
    return sol

def answer(subway): 
    sol = hasMeetingPoint(subway)
    if sol == -1:
        return -1
    else:
        n = len(subway)
        for i in range(0,n):
            newSubway = copy.deepcopy(subway);
            newSubway = closeStation(newSubway,i)
            sol = hasMeetingPoint(newSubway)
            if sol == -1:
                return i
    return -2

    
subway = [[2, 1], [2, 0], [3, 1], [1, 0]]
print(answer(subway))
    
subway = [[1, 2], [1, 1], [2, 2]]
print(answer(subway))

subway = [[0, 0], [1, 1],  [2, 2]]
print(answer(subway))

print('Random subway')
m = 5
n = 50
subway = []

for k in range(0,n):
    subway.append(random.sample(range(0, n), m))
print(answer(subway))

