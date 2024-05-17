def Multiply(A,B):
    result = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][j] * B[i][j]
    for p in result:
        print(p)
    return 0
A = [[0,0,3], [7,7,7], [3,0,0]]
B = [[4,5,10], [5,1,0], [13,2,10]]
print("resultant matrix: ")
Multiply(A,B)