def matMult(mat1, mat2):
    n = len(mat1)
    res = [[0 for col in range(n)] for row in range(n)]
    for row in range(n):
        for col in range(n):
                for i in range(n):
                    res[row][col] += mat1[row][i] * mat2[i][col]   
    return res
            
mat1 = [[1,2],[3,4]]
mat2 = [[5,6],[7,8]]
res = matMult(mat1, mat2)
print(res)

#With numpy
import numpy as np
npMat1 = np.array(mat1)
npMat2 = np.array(mat2)
npRes = np.matmul(npMat1, npMat2)
print(npRes)