def answer(seq):
    # your code here
    # first number r can't change 
    # we have two group of numbers A, B
    # where, A > r (left numbers) , B < r (Right numbers)
    # C1: count the number  possibilities in a group numbers (A or B)
    # C1: answer(B) * answer(A)
    # C2: count the number of interleaving possibilities between group A and B. 
    # C2: Comb(elmA+elmB, elmB) where elmA and elmB is the number of elements in A and B 
    fact = lambda x: 1 if x == 0 else x * fact(x-1)
    comb = lambda n, r: 0 if r > n  else fact(n)/(fact(n-r)*fact(r))
    
    r = seq[0]
    elmA = 0
    elmB = 0
    A = []
    B = []
    
    for i in range(1, len(seq)):
        if seq[i] > r:
            A.append(seq[i]);
        else:
            B.append(seq[i]);
            
    elmA = len(A)
    elmB = len(B)
    if elmA > 0 and elmB > 0:
        C2 = answer(A) * answer(B)
    elif elmA == 0 and elmB >0:
        C2 = 1* answer(B)
    elif elmA > 0 and elmB == 0:
        C2 = answer(A) * 1
    else:
        return 1
        
    C1 = comb(elmA + elmB, elmA)
    
    return C1 * C2