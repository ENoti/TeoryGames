import copy
import matrix
import numpy as np

def maximin(matr: matrix.Matrix, param):
    arr = np.empty(matr.n, dtype=object) 
    minElem = matr.matrix[0][0][param]
    #Первый игрок имеет параметр = 0
    if(param == 0):
        for i in range (matr.n):
            minElem = matr.matrix[i][0][param]
            for j in range (matr.m):
                #Проходимся по элементам строки, и выбираем минимальное
                if matr.matrix[i][j][param] < minElem:
                    minElem = matr.matrix[i][j][param]
            #Добавляем в массив все минимальные значения по всем строкам
            arr[i] = minElem
        maxElem = arr[0]
        #Находим максимальное из минимальных
        for i in range(arr.size):
            if arr[i] > maxElem:
                maxElem = arr[i]
    #Второй игрок имеет параметр = 1
    elif(param == 1):
        for i in range (matr.m):
            minElem = matr.matrix[0][i][param]
            for j in range (matr.n):
                #Проходимся по элементам столбца, и выбираем минимальное
                if matr.matrix[j][i][param] < minElem:
                    minElem = matr.matrix[j][i][param]
            #Добавляем в массив все минимальные значения по всем столбцам
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
        #Сравниваем текущую строчку со всеми следующими
        for k in range(n - 1):
            for i in range(k + 1, n):
                chet1 = 0
                chet2 = 0
                #Происходит сравнение всех значений строчки с другой строчкой
                for j in range(m):
                    if matr.matrix[k][j][param] < matr.matrix[i][j][param]:
                        chet1 += 1
                    elif matr.matrix[k][j][param] > matr.matrix[i][j][param]:
                        chet2 += 1
                #Если они были строго больше/меньше, то добавляем их для удаления
                if chet1 == m:
                    if k not in index:
                        index.append(k)
                elif chet2 == m:
                    if i not in index:
                        index.append(i)
        if len(index) == 0:
            print("Строго доминируемых стратегий не обнаружено")
            return matr
        index.sort(reverse=True)
        #Создаем копию матрицы и удаляем все строгодоминирующие позиции
        newMatrix = copy.deepcopy(matr)
        new_n = matr.n
        for i in range(n):
            if i not in index:
                newMatrix.matrix = np.delete(newMatrix.matrix, i, 0)
                del newMatrix.first_player_strategies[i]
                new_n-=1
        newMatrix.n = new_n
    elif (param == 1):
        #Сравниваем текущий столбец со всеми следующими
        for k in range(m - 1):
            for i in range(k + 1, m):
                chet1 = 0
                chet2 = 0
                #Происходит сравнение всех значений столбца с другим столбцом
                for j in range(n):
                    if matr.matrix[j][k][param] < matr.matrix[j][i][param]:
                        chet1 += 1
                    elif matr.matrix[j][k][param] > matr.matrix[j][i][param]:
                        chet2 += 1
                #Если они были строго больше/меньше, то добавляем их для удаления
                if chet1 == n:
                    if k not in index:
                        index.append(k)
                elif chet2 == n:
                    if i not in index:
                        index.append(i)
        if len(index) == 0:
            print("Строго доминируемых стратегий не обнаружено")
            return matr
        index.sort(reverse=True)
        #Создаем копию матрицы и удаляем все строгодоминирующие позиции
        newMatrix = copy.deepcopy(matr)
        new_m = matr.m
        for i in range(m):
            if i not in index:
                newMatrix.matrix = np.delete(newMatrix.matrix, i, axis=1)
                del newMatrix.second_player_strategies[i]
                new_m -= 1
        newMatrix.m = new_m

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
        if len(index) == 0:
            print("Слабо доминирующая стратегий не обнаружено")
            return matr
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
        if len(index) == 0:
            print("Слабо доминирующая стратегий не обнаружено")
            return matr
        index.sort(reverse=True)
        newMatrix = copy.deepcopy(matr)
        new_m = matr.m
        for i in range(m):
            if i not in index:
                newMatrix.matrix = np.delete(newMatrix.matrix, i, axis=1)
                del newMatrix.second_player_strategies[i]
                new_m -= 1
        newMatrix.m = new_m

    return newMatrix

def nesh(matr: matrix.Matrix):
    n = matr.n
    m = matr.m
    index_i = 0
    index_j = 0
    maxElem  = matr.matrix[0][0][0]
    #Создаем нулевую матрицу размером нашей матрицы
    newMatr = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            #Проходимся по строчке и ищем максимальное значение, после запоминаем его индексы
            if maxElem <= matr.matrix[i][j][0]:
                maxElem = matr.matrix[i][j][0]
                index_i = i
                index_j = j
        maxElem = matr.matrix[i][0][0]
        #В нулевой матрице реализуем счетчик, где был найден макс элемент
        newMatr[index_i][index_j] += 1
    maxElem  = matr.matrix[0][0][0]
    for i in range(m):
        for j in range(n):
            #Проходимся по столбце и ищем максимальное значение, после запоминаем его индексы
            if maxElem <= matr.matrix[j][i][1]:
                maxElem = matr.matrix[j][i][1]
                index_i = i
                index_j = j
        maxElem = matr.matrix[0][j][1]
        #В нулевой матрице реализуем счетчик, где был найден макс элемент
        newMatr[index_j][index_i] += 1
    for i in range(n):
        for j in range(m):
            #Если по заданному индексу для обоих игроков лучший вариант, значит игра равновесна
            if(newMatr[i][j] == 2):
                return i, j
    print("Невозможно равновесие по Нэшу")
    return None
