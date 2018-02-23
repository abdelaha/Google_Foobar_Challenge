import fractions as fs
__author__ = 'Hamzah'
def areaOnly(vertices):
    # your code here
    A = vertices[0] 
    B = vertices[1]
    C = vertices[2]
    #Just for fun
    area = float((A[0]*(B[1]-C[1])) + (B[0]*(C[1] - A[1])) +(C[0]*(A[1]-B[1]))) /2
    area = abs(area)
    return area


def answer(vertices):
    # your code here
    A = vertices[0]
    B = vertices[1]
    C = vertices[2]
    #Just for fun
    area = float((A[0]*(B[1]-C[1])) + (B[0]*(C[1] - A[1])) +(C[0]*(A[1]-B[1]))) / 2
    area = abs(area)
    latticePoint = abs(fs.gcd(B[0]-A[0],B[1]-A[1])) 
    latticePoint += abs(fs.gcd(C[0]-A[0],C[1]-A[1])) 
    latticePoint += abs(fs.gcd(C[0]-B[0],C[1]-B[1])) 
    
    # Using Pick's theorem A = i + b/2 - 1
    # i = A +1 - b/2
    
    sol = area + 1 - float(latticePoint /2)
    return int(sol)
	
	
vertices = [[2, 3], [6, 9], [10, 160]]
aa = areaOnly(vertices)
print(aa)
aa = answer(vertices)
print(aa)

vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
aa = areaOnly(vertices)
print(aa)
aa = answer(vertices)
print(aa)

vertices = [[1, 0], [0,1], [-1, -1]]
aa = areaOnly(vertices)
print(aa)
aa = answer(vertices)
print(aa)

vertices = [[2, 4], [8,0], [-2, -2]]
aa = areaOnly(vertices)
print(aa)
aa = answer(vertices)
print(aa)
