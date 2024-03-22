import domain.matrix as matrix
import numpy as np

def minimax(matr: matrix.Matrix):
    arr = np.empty(matr.n, dtype=object) 
    minElem = matr.matrix[0][0]
    for i in range (matr.n):
        for j in range (matr.m):
            if matr[i][j] < minElem:
                minElem = matr[i][j]
        arr[i] = minElem
    maxElem = arr[0]
    for i in range(arr.size):
        if arr[i] > maxElem:
            maxElem = arr[i]
    return maxElem


def maximin(matr: matrix.Matrix):
    arr = np.empty(matr.n, dtype=object) 
    minElem = matr.matrix[0][0]
    for i in range (matr.n):
        for j in range (matr.m):
            if matr.matrix[i][j] > minElem:
                minElem = matr[i][j]
        arr[i] = minElem
    maxElem = arr[0]
    for i in range(arr.size):
        if arr[i] < maxElem:
            maxElem = arr[i]
    return maxElem

def dominant(matr: matrix.Matrix):
    newMatr= np.copy(matr)
    
    for i in range(matr.n):
        for j in range(matr.m):
            if all(newMatr[i, k] <= matr[i, j] for k in range(matr.m) if k != j) and all(newMatr[k, j] >= matr[i, j] for k in range(matr.n) if k != i):
                newMatr[i, j] = 0
                
    return newMatr
    
def weaklyDominant(matr: matrix.Matrix):
    newMatr = np.copy(matr)
    
    for i in range(matr.n):
        for j in range(matr.m):
            if all(newMatr[i, k] < matr[i, j] for k in range(matr.m) if k != j) and all(newMatr[k, j] > matr[i, j] for k in range(matr.n) if k != i):
                newMatr[i, j] = 0
                
    return newMatr    

matr = matrix.Matrix.input_from_file('TeoryGames/matrix.txt')
print(minimax(matr))
#print(minimax(matr))


