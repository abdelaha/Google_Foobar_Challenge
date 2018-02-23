def answer(x):
    # your code here
    
    # assume no fault detection, x has to be int greater than 0
    # Algorithm 
    # Step1: make x to be dividable by 3 by either add/sub one from it
    #        sub mean add 1 to Right side. y = x +/- 1
    # Step2: recursive algorithm (R,L)
        #2.1 calculate the largest weight that will use to balance |L-R|
        #2.2 if L> R, put it in R then go to 2.1
        #2.2 if L< R, put it in L then go to 2.1
        #2.2 if L == R, return
    # DataStructure:
    # strList : the output stringlist
    # R : Weight in the Right Side
    # L : Weight in the Left Side
    
    
    #note this is a pseudo code
    #initialization
    strList = []
    R = 0
    L = x
    listInitFlag = 0
    
    #Step 1  
    if x % 3 == 2:   #add one to x
        strList.insert(0,"L")
        L += 3**0
    elif x % 3 == 1: #sub one to x 
        strList.insert(0,"R")
        R += 3**0
    else:
        strList.insert(0,"-")
    
    #Step 2: Implement the following algorithm recursively  till L-R = 0
    while L != R:
        #2.1 calculate the largest weight we need to use,
        # it is the smallest weight(n) such that \sum_n {3**n} >= diff
        # on other word: min_n[\sum_n {3**n}]  subject to \sum_n {3**n} >= diff
        diff = abs(L-R)
        indx = 1
        WeightSum = 3**indx
        while WeightSum < diff:
            indx += 1
            WeightSum += 3**indx
        
        #if this is the first loop, then we know the size of strList, so init it
        if listInitFlag  == 0:
            listInitFlag = 1
            strList += ["-"] * indx
        #add the largest weight in the lightest side
        if L < R:
            L += 3**indx
            strList[indx] = "L"
        else:
            R += 3**indx
            strList[indx] = "R"
            
        
    return strList
    
    
l = answer(89)    