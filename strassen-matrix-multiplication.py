import numpy as np

def matMult(mat1, mat2):
    n = len(mat1)
    if(n <= 1):
        return np.array([[mat1[0][0] * mat2[0][0]]])
    
    nby2 = n//2    
    a = mat1[:nby2, :nby2]
    b = mat1[:nby2, nby2:]
    c = mat1[nby2:, :nby2]
    d = mat1[nby2:, nby2:]
    e = mat2[:nby2, :nby2]
    f = mat2[:nby2, nby2:]
    g = mat2[nby2:, :nby2]
    h = mat2[nby2:, nby2:]

    p1 = matMult(a, f - h)
    p2 = matMult(a + b, h)
    p3 = matMult(c + d, e)
    p4 = matMult(d, g - e)
    p5 = matMult(a + d, e + h)
    p6 = matMult(b - d, g + h)
    p7 = matMult(a - c, e + f)
    
    row1 = np.concatenate((p5 + p4 - p2 + p6, p1 + p2), axis = 1)
    row2 = np.concatenate((p3 + p4, p1 + p5 - p3 - p7), axis = 1)
    res = np.concatenate((row1, row2), axis = 0)
    return res
#            
mat1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
mat2 = [[17,18,19,20],[21,22,23,24],[25,26,27,28],[29,30,31,32]]
mat1 = np.array(mat1)
mat2 = np.array(mat2)
res = matMult(mat1, mat2)
print(res)
npRes = np.matmul(mat1, mat2)
print(npRes)