import sys
import copy

def create_matrix_sumizh():
    file = open('File.txt')
    info = file.readline()
    info_size = info.split(" ")
    count_versh_half = (int(info_size[0])) // 2
    if ((int(info_size[0]) == 0) and (int(info_size[1]) == 0)) or (int(info_size[0]) == 0) or int(
            info_size[0]) % 2 != 0:
        sys.exit("Помилка! Не існує досконалих паросполучень!")
    else:
        matrix_sumizh = [[0] * (int(info_size[0]) // 2) for x in range(int(info_size[0]) // 2)]
        for i in range(int(info_size[1])):
            info_versh = file.readline()
            info_versh_arr = info_versh.split(" ")
            matrix_sumizh[(int(info_versh_arr[0]) % count_versh_half) - 1][
                (int(info_versh_arr[1]) % count_versh_half) - 1] = 1
        file.close()
        return matrix_sumizh


def output(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(" ", matrix[i][j], end=' ')
        print()
    return matrix


def initialization(matrix):
    matrix_new = [['*'] * len(matrix) for x in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                matrix_new[i][j] = "1"

    return matrix_new

def parospolychenya(matrix):
    for i in range(len(matrix)):
        counter = 0
        for j in range(len(matrix)):
            if matrix[i][j] == "1":
                counter += 1
                if counter == 1:
                    continue
                elif counter >= 1:
                    matrix[i][j] = 0
            else:
                continue
    return matrix


def perevirka(matrix):
    global counter1
    arr = []
    for i in range(len(matrix)):
        count = 0
        for j in range(len(matrix)):
            if matrix[j][i] == 1:
                count += 1
        arr.append(count)
    counter = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            counter += 1
    if counter == len(arr):
        print("%s_Матр. доск. паросполучень" %counter1)
        counter1 += 1
        output(matrix)
        arr = []
    else:
        arr = []


def deleteOnes(matrix):
    for line in matrix:
        for i in range(len(line)):
            if line[i] != "*":
                line[i] = 0


def printRecurs(matrix, numberOfLine):
    if numberOfLine >= len(matrix):
        perevirka(matrix)
        return

    for i in range(0, len(matrix[0])):
        if matrix[numberOfLine][i] != "*":
            newMatrix = copy.deepcopy(matrix)
            if newMatrix[numberOfLine][i] != "*":
                newMatrix[numberOfLine][i] = 1
                printRecurs(newMatrix, numberOfLine + 1)


counter1 = 1
matrix1 = create_matrix_sumizh()
matr = initialization(matrix1)
m1 = parospolychenya(matr)
deleteOnes(m1)
printRecurs(m1, 0)

