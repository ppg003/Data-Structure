# -*- coding:utf-8 -*-
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s : %(message)s"
)


def print_chess(chess):
    dic = {
        0: ".",
        1: "X",
    }
    for i in range(len(chess)):
        for j in range(len(chess[0])):
            print(dic[chess[i][j]], end=" ")
        print("")
    print("")


def isSafe(x, y, matrix):
    # row
    for col in range(y):
        if matrix[x][col] == 1:
            return False

    # column
    for row in range(x):
        if matrix[row][y] == 1:
            return False

    # duijiaoxian - na
    if x - y < 0:
        row = 0
        col = y - x
    elif x - y > 0:
        row = x - y
        col = 0
    else:
        row, col = 0, 0

    while row < len(matrix) and col < len(matrix[0]):
        if row != x:
            if matrix[row][col] == 1:
                return False
        row += 1
        col += 1

    # duijiaoxian - pie - xia
    for row, col in zip(range(x + 1, len(matrix)), range(y - 1, -1, -1)):
        if matrix[row][col] == 1:
            return False

    # duijiaoxian - pie - shang
    for row, col in zip(range(x - 1, -1, -1), range(y + 1, len(matrix))):
        if matrix[row][col] == 1:
            return False

    return True


def n_huanghou(row, n, chess):
    global count
    che2 = [[chess[i][j] for j in range(n)] for i in range(n)]
    if row == n:
        # print("No.%s" % (count + 1))
        print_chess(che2)
        count += 1
    else:
        found = False
        for col in range(n):
            for i in range(len(che2[row])):
                che2[row][i] = 0
            # print("Row : %s, Col : %s" % (row + 1, col + 1))
            # print_chess(che2)
            if isSafe(row, col, che2):
                found = True
                # print("Row : %s, Col : %s is available" % (row + 1, col + 1))
                che2[row][col] = 1
                n_huanghou(row + 1, n, che2)
        if not found:
            pass
            # print("Give up this try.")


def go(n):
    global count
    count = 0
    chess = [[0 for i in range(n)] for i in range(n)]
    # print_chess(chess)
    n_huanghou(0, n, chess)
    print("Total : %s" % count)


go(11)
