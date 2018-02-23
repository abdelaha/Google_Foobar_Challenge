def answer_bruteForce(s,x):
    # your code here
    # Hints:
    #   For a given s:
    #   the number of combination is le s+1, and the combinations are (s-n,n)
    #   where n = 0, 1, 2, ... s
  
    #   special case: (s == 0)
    #   
    ## Brute force approach (VERY SIMPLE BUT VERY SLOW)
    if x == 0:
        if s%2 ==0:     #the only valid pairs is (s/2, s/2)
            return 1
        else:
            return 0
    if s == x:   #the following pairs are valid (s,0) and (0,s)
        numOfComb = 2        
    else:
        numOfComb = 0
                
    n = s/2
    for i in range(1, n+1):
        if i^(s-i) == x:
            if s-i==i:
                numOfComb += 1
            else:
                numOfComb += 2
    
    # get the component
    
    #remove it from s and x
    
    #check
    #repeat till x == 0
    
       
    return numOfComb  
	
# submitted optimized solution	
def answer(s,x):
    # your code here
    # Hints:
    #   the ones in x shows the 2^i component that can exist in one of each pair
    # Algorithm:
    # 1. Get the first one index i in x
    # 2. x = s- 2^i, s = s - 2^i
    # 3. update the number of combination power numOfComb ++
    # 4. check for termination condition (when x ==0)
            # s has to be non-negative
            # s has to be dividable over two 
            # s can't have 2^i elements in x.
    # 5. repeat for answer(newS,NewX)
    
    #special Case
    if x == 0:
        if s%2 ==0:     #the only valid pairs is (s/2, s/2)
            return 1
        else:
            return 0
    
    #initialization
    numOfComb = 0
    newx = x
    while(bin(newx).count("1") >0):
        #1. Get the first one index i in x
        strx = bin(newx)     # convert to binary string
        strx = strx[2:]   # remove 0b
        i = strx.index("1")  #index of the first one from the left
        i =  len(strx)- i-1  #index of the same one but counting from right
        # 2. 
        newx = newx - 2**i 
        s = s - 2**i
        # 3. 
        numOfComb +=1
        # 4. termination invalid check
        if s < 0:
            return 0
    # 4. termination conditions
    if newx == 0:
        if s%2 ==0 and (s/2)&x ==0:     #There are valid compilations that can result in s,x
            return 2**numOfComb
        else:
            return 0
        
         
                                
         
        
             
    
answer(100,40)
            
                          
        