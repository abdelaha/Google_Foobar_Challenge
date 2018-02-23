__author__ = 'Hamzah'
# used for memorizing binomial coefficient
globalR = {}
    
    
def R(x):
    if x in globalR:
        res = globalR[x]
    else:
        if x <= 1 :
            res = 1
        elif x == 2:
            res = 2
        elif x % 2 == 0:
            n = x/2
            res = (R(n) + R(n+1) + n)
        else:
            n = (x-1)/2
            res = R(n-1) + R(n) +1
            if n-1 in globalR:
                del globalR[n-1]
        globalR[x] = res
    return res
    
    
def answer(str_S):
    # your code here
    # Series analysis
    # numbers with odd index  never get repeated
    # number with even index never get repeated
    # both even/odd index series are increasing
    # even series are always larger than the odd ones. 
    # we can ignore memorizing any number under R(n-1) if we search incrementally
    
    #Apply binary search using the odd series to determine the range that you could search in.
    
	
	#pilot points
    
    minO = 0
    maxO = 10**25
    minE = minO
    maxE = maxO
    
    #binary search 
    s = int(str_S)
 
    indx = -1
    oddDone = 0
    evenDone = 0
    while evenDone == 0 or oddDone  ==0 :
        
        if evenDone == 0:
            p =  (maxE-minE)>>1
            midE = minE +p
            midE = midE >> 1
            midE = midE << 1
            n1 = R(midE)
            
            if s == n1:
                indx = midE
                evenDone = 1
                n1 = -1
            elif n1 < s:
                minE = midE + 2
            else:
                maxE = midE - 2
                
            if maxE < minE:
                evenDone = 1
            
    
        if oddDone == 0:
            p = (maxO - minO)>>1
            midO = (minO + p) | 1
            n2 = R(midO)
            
            if s == n2:
               return midO
            elif n2 < s:
                minO = midO + 2
            else:
                maxO = midO - 2
                
            if maxO < minO:
                oddDone = 1
        
        
                        
                    
                    
                    
    if indx == -1:
        return 'None'        
    else:
        return indx
        
        
        
answer('100')