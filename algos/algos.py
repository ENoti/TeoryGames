import matrix
import numpy as np

def maximin(matr: matrix.Matrix, param):
    arr = np.empty(matr.n, dtype=object) 
    minElem = matr.matrix[0][0][param]
    if(param == 0):
        for i in range (matr.n):
            for j in range (matr.m):
                if matr.matrix[i][j][param] < minElem:
                    minElem = matr.matrix[i][j][param]
            arr[i] = minElem
            minElem = matr.matrix[i][0][param]
        maxElem = arr[0]
        for i in range(arr.size):
            if arr[i] > maxElem:
                maxElem = arr[i]
    elif(param == 1):
        for i in range (matr.n):
            for j in range (matr.m):
                if matr.matrix[j][i][param] < minElem:
                    minElem = matr.matrix[j][i][param]
            arr[i] = minElem
            minElem = matr.matrix[0][j][param]
        maxElem = arr[0]
        for i in range(arr.size):
            if arr[i] > maxElem:
                maxElem = arr[i]
    return maxElem

def minimax(matr: matrix.Matrix, param):
    arr = np.empty(matr.n, dtype=object) 
    minElem = matr.matrix[0][0][param]
    if(param == 0):
        for i in range (matr.n):
            for j in range (matr.m):
                if matr.matrix[i][j][param] > minElem:
                    minElem = matr.matrix[i][j][param]
            arr[i] = minElem
            minElem = matr.matrix[i][0][param]
        maxElem = arr[0]
        for i in range(arr.size):
            if arr[i] < maxElem:
                maxElem = arr[i]
    elif(param == 1):
        for i in range (matr.n):
            for j in range (matr.m):
                if matr.matrix[j][i][param] > minElem:
                    minElem = matr.matrix[j][i][param]
            arr[i] = minElem
            minElem = matr.matrix[0][j][param]
        maxElem = arr[0]
        for i in range(arr.size):
            if arr[i] < maxElem:
                maxElem = arr[i]
    return maxElem

def dominant(matr: matrix.Matrix, param):
    newMatr = matr.matrix
    index = []
    n = matr.n
    m = matr.m
    if (param == 0):
        for k in range(n - 1):
            for i in range(k + 1, n):
                chet1 = 0
                chet2 = 0
                for j in range(m):
                    if matr.matrix[k][j][param] < matr.matrix[i][j][param]:
                        chet1 += 1
                    elif matr.matrix[k][j][param] > matr.matrix[i][j][param]:
                        chet2 += 1
                
                if chet1 == m:
                    if k not in index:
                        index.append(k)
                elif chet2 == m:
                    if i not in index:
                        index.append(i)
        index.sort(reverse=True)
        for i in index:
            for j in range (m):
                np.delete(newMatr, i, j)
    elif (param == 1):
        for k in range(n - 1):
            for i in range(k + 1, n):
                chet1 = 0
                chet2 = 0
                for j in range(m):
                    if matr.matrix[j][k][param] < matr.matrix[j][i][param]:
                        chet1 += 1
                    elif matr.matrix[k][j][param] > matr.matrix[j][i][param]:
                        chet2 += 1
                
                if chet1 == m:
                    if k not in index:
                        index.append(k)
                elif chet2 == m:
                    if i not in index:
                        index.append(i)
        index.sort(reverse=True)
        for i in index:
            for j in range (n):
                np.delete(newMatr, j, i)

    if len(index) == 0:
        print("Строго доминируемых стратегий не обнаружено")
        newMatr = None

    return newMatr

def weaklyDominant(matr: matrix.Matrix, param):
    newMatr = matr.matrix
    index = []
    n = matr.n
    m = matr.m
    if (param == 0):
        for k in range(n - 1):
            for i in range(k + 1, n):
                chet1 = 0
                chet2 = 0
                for j in range(m):
                    if matr.matrix[k][j][param] <= matr.matrix[i][j][param]:
                        chet1 += 1
                    if matr.matrix[k][j][param] >= matr.matrix[i][j][param]:
                        chet2 += 1
                if chet1 == m and k not in index:
                    index.append(k)
                if chet2 == m and i not in index:
                    index.append(i)
        index.sort(reverse=True)
        if index:
            for i in index:
                newMatr = np.delete(newMatr, i, 0)
    elif (param == 1):
        for k in range(n - 1):
            for i in range(k + 1, n):
                chet1 = 0
                chet2 = 0
                for j in range(m):
                    if matr.matrix[j][k][param] <= matr.matrix[j][i][param]:
                        chet1 += 1
                    if matr.matrix[j][k][param] >= matr.matrix[j][i][param]:
                        chet2 += 1
                if chet1 == m and k not in index:
                    index.append(k)
                if chet2 == m and i not in index:
                    index.append(i)
        index.sort(reverse=True)
        if index:
            for i in index:
                newMatr = np.delete(newMatr, i, 0)

    if len(newMatr) == len(matr.matrix):
        print("Слабо доминируемых стратегий не обнаружено")

    return newMatr 

def nesh(matr: matrix.Matrix):
    n = matr.n
    m = matr.m
    index_i = 0
    index_j = 0
    maxElem  = matr.matrix[0][0][0]
    newMatr = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            if maxElem < matr.matrix[i][j][0]:
                maxElem = matr.matrix[i][j][0]
                index_i = i
                index_j = j
        maxElem = matr.matrix[i][0][0]
        newMatr[index_i][index_j] += 1
    for i in range(n):
        for j in range(m):
            if maxElem < matr.matrix[j][i][1]:
                maxElem = matr.matrix[j][i][1]
                index_i = i
                index_j = j
        maxElem = matr.matrix[0][j][1]
        newMatr[index_i][index_j] += 1
    for i in range(n):
        for j in range(m):
            if(newMatr[i][j] == 2):
                return i, j
    print("Невозможно равновесие по Нэшу")
    return i, j

matr = matrix.Matrix.input_from_file('TeoryGames/matrix.txt')
print(maximin(matr, 1))


