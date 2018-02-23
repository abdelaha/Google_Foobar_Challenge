def answer(N, K):
	# your code here
    """
	# (N-1) <= k <= (N * (N-1))/2
    # a <= k <= b
    # this condition ensure that it is always possible to build
    # a path between all the warrens and it is always possible to use all
    # the tunnels k = b without connecting two warrens with two tunnels. 
    #
    # Data Structure:
    # b,c as constant
    # n = b - a
    # r = k - a
    #
    # Algorithm
    # the algorithm is two cases:
	# Easy case: K >= ((N-1) * (N-2))/2  which mean any kind of graph is connection simple graph. all condition is not violated in any case
	# Trouble case: otherwise, 			 which mean that there are some invalid graphs that violate the required constraints. 
	#										1. floating warren(s)
	#										2. there are no path between two or more group of warrens. (in-connecting graphs)
    # sol = possible number of choosing k tunnels from b [b C k] - invalidCases
    #       
	"""
    fact = lambda x: 1 if x == 0 else x * fact(x-1)
    comb = lambda n, r: 0 if r > n  else fact(n)/(fact(n-r)*fact(r))
    countn = lambda n, k : 0 if k > ((n-1) * (n-2))/2 else 1 # + countn(n-1, k)

    b = (N * (N-1))/2
    c = countn(N, K)
    if K < N - 1:
        sol = 0
    elif K > b:
        sol = 0
    elif K == b:
        sol = 1
    elif K == N-1: # Cayley's formula  (tree not graph)
        sol = int(N ** (N-2))
    else:
        if c == 0:
            invalid = 0
        else :
            invalid = 0
            for i in range(1,N-2):
                flagInvalid = invalid 
                tmp = (i*(i-1)>>1)
                if tmp < K:
                    k = tmp
                else:
                    k = K
                a = i*(i-1)/2
                tmp = comb(N,i)
                for j in range(0, k+1):
                    # Number of choosing i node from N -by- number of connected labeled graph in (N-i,K-j) -by- number of choosing tunnel from a
                    if i > N>>1:   # to avoid re calculated two connected graphs of size (i and N-i)
                        tmp2 = comb(a,j) - int(answer(i,j)) # this to calculate more than two connected graphs one of them of size N-i
                    else:
                        tmp2 =  comb(a,j)  # this to calculate more than one connected graphs one of them of size (N-i)
                    invalid += tmp * int(answer(N-i,K-j)) * tmp2
                if i > (N>>1) and flagInvalid == invalid:
                    break
        sol = comb(b, K) - invalid

    return "%d" %  sol