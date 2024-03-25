import copy
import matrix
import numpy as np

def maximin(matr: matrix.Matrix, param):
    arr = np.empty(matr.n, dtype=object) 
    minElem = matr.matrix[0][0][param]
    if(param == 0):
        for i in range (matr.n):
            minElem = matr.matrix[i][0][param]
            for j in range (matr.m):
                if matr.matrix[i][j][param] < minElem:
                    minElem = matr.matrix[i][j][param]
            arr[i] = minElem
        maxElem = arr[0]
        for i in range(arr.size):
            if arr[i] > maxElem:
                maxElem = arr[i]
    elif(param == 1):
        for i in range (matr.m):
            minElem = matr.matrix[0][i][param]
            for j in range (matr.n):
                if matr.matrix[j][i][param] < minElem:
                    minElem = matr.matrix[j][i][param]
            arr[i] = minElem
    return max(arr)

def minimax(matr: matrix.Matrix, param):
    arr = np.empty(matr.n, dtype=object) 
    minElem = matr.matrix[0][0][param]
    if(param == 0):
        for i in range (matr.n):
            minElem = matr.matrix[i][0][param]
            for j in range (matr.m):
                if matr.matrix[i][j][param] > minElem:
                    minElem = matr.matrix[i][j][param]
            arr[i] = minElem
        maxElem = arr[0]
        for i in range(arr.size):
            if arr[i] < maxElem:
                maxElem = arr[i]
    elif(param == 1):
        for i in range (matr.m):
            minElem = matr.matrix[0][i][param]
            for j in range (matr.n):
                if matr.matrix[j][i][param] > minElem:
                    minElem = matr.matrix[j][i][param]
            arr[i] = minElem
    return min(arr)

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
        newMatrix = copy.deepcopy(matr)
        new_n = matr.n
        for i in range(n):
            if i not in index:
                newMatrix.matrix = np.delete(newMatrix.matrix, i, 0)
                del newMatrix.first_player_strategies[i]
                new_n-=1
        newMatrix.n = new_n
    elif (param == 1):
        for k in range(m - 1):
            for i in range(k + 1, m):
                chet1 = 0
                chet2 = 0
                for j in range(n):
                    if matr.matrix[j][k][param] < matr.matrix[j][i][param]:
                        chet1 += 1
                    elif matr.matrix[j][k][param] > matr.matrix[j][i][param]:
                        chet2 += 1
                
                if chet1 == n:
                    if k not in index:
                        index.append(k)
                elif chet2 == n:
                    if i not in index:
                        index.append(i)
        index.sort(reverse=True)
        newMatrix = copy.deepcopy(matr)
        new_m = matr.m
        for i in range(m):
            if i not in index:
                newMatrix.matrix = np.delete(newMatrix.matrix, i, axis=1)
                del newMatrix.second_player_strategies[i]
                new_m -= 1
        newMatrix.m = new_m

    if len(index) == 0:
        print("Строго доминируемых стратегий не обнаружено")
        newMatr = None

    return newMatrix

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
                    elif matr.matrix[k][j][param] >= matr.matrix[i][j][param]:
                        chet2 += 1
                
                if chet1 == m:
                    if k not in index:
                        index.append(k)
                elif chet2 == m:
                    if i not in index:
                        index.append(i)
        index.sort(reverse=True)
        newMatrix = copy.deepcopy(matr)
        new_n = matr.n
        for i in range(n):
            if i not in index:
                newMatrix.matrix = np.delete(newMatrix.matrix, i, 0)
                del newMatrix.first_player_strategies[i]
                new_n-=1
        newMatrix.n = new_n
    elif (param == 1):
        for k in range(m - 1):
            for i in range(k + 1, m):
                chet1 = 0
                chet2 = 0
                for j in range(n):
                    if matr.matrix[j][k][param] <= matr.matrix[j][i][param]:
                        chet1 += 1
                    elif matr.matrix[j][k][param] >= matr.matrix[j][i][param]:
                        chet2 += 1
                
                if chet1 == n:
                    if k not in index:
                        index.append(k)
                elif chet2 == n:
                    if i not in index:
                        index.append(i)
        index.sort(reverse=True)
        newMatrix = copy.deepcopy(matr)
        new_m = matr.m
        for i in range(m):
            if i not in index:
                newMatrix.matrix = np.delete(newMatrix.matrix, i, axis=1)
                del newMatrix.second_player_strategies[i]
                new_m -= 1
        newMatrix.m = new_m

    if len(index) == 0:
        print("Слабо доминирующая стратегий не обнаружено")
        newMatr = None

    return newMatrix

def nesh(matr: matrix.Matrix):
    n = matr.n
    m = matr.m
    index_i = 0
    index_j = 0
    maxElem  = matr.matrix[0][0][0]
    newMatr = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            if maxElem <= matr.matrix[i][j][0]:
                maxElem = matr.matrix[i][j][0]
                index_i = i
                index_j = j
        maxElem = matr.matrix[i][0][0]
        newMatr[index_i][index_j] += 1
    maxElem  = matr.matrix[0][0][0]
    for i in range(m):
        for j in range(n):
            if maxElem <= matr.matrix[j][i][1]:
                maxElem = matr.matrix[j][i][1]
                index_i = i
                index_j = j
        maxElem = matr.matrix[0][j][1]
        newMatr[index_j][index_i] += 1
    for i in range(n):
        for j in range(m):
            if(newMatr[i][j] == 2):
                return i, j
    print("Невозможно равновесие по Нэшу")
    return None
