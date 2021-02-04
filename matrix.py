def rotate(matrix):
    n = len(matrix)
    # 转置矩阵
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 翻转矩阵

    for i in range(n):
        for j in range(i, n // 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


def spiralOrder(matrix):
    ans = []
    u = 0
    d = len(matrix) - 1
    l = 0
    r = len(matrix) - 1
    while True:
        for i in range(l, r + 1):
            ans.append(matrix[u][i])

        u += 1
        if u > d:
            break

        for i in range(u, d + 1):
            ans.append(matrix[i][r])

        r -= 1
        if r < l:
            break

        for i in range(r, l - 1, -1):
            ans.append(matrix[d][i])

        d -= 1
        if d < u:
            break

        for i in range(d, u - 1, -1):
            ans.append(matrix[i][l])

        l += 1
        if l > r:
            break

    return ans


def direction(pre_point, pre_direct, step, border):
    up = 1
    down = 2
    left = 3
    right = 4
    x, y = pre_point
    if pre_direct == right:
        tmp = y + 1
        if tmp < border:
            return right, right, [pre_point[0], tmp], step, border

        else:
            return right, down, [pre_point[0], tmp], step, x + step

    if pre_direct == down:
        tmp = x + 1
        if tmp < border:
            return down, down, [tmp, pre_point[1]], step, border
        else:
            step = step + 1
            return down, left, [tmp, pre_point[1]], step, y - step

    if pre_direct == left:
        tmp = y - 1
        if tmp > border:
            return left, left, [pre_point[0], tmp], step, border
        else:
            return left, up, [pre_point[0], tmp], step, x - step

    if pre_direct == up:
        tmp = x - 1
        if tmp > border:
            return up, up, [tmp, pre_point[1]], step, border
        else:
            step = step + 1
            return up, right, [tmp, pre_point[1]], step, y + step


def set_value(point, matrix, value):
    matrix[point[0]][point[1]] = value


def generateMatrix(n):
    """
    从中心点开始生成顺时针旋转矩阵
    :param n:
    :return:
    """
    step = 1
    border = 1

    matrix = [[0 for _ in range(n)] for _ in range(n)]
    center = (n - 1) // 2

    next_dirction = cur_direction = 4
    point = []

    for i in range(1, n * n + 1):
        if i == 1:
            point = [center, center]
            set_value(point, matrix, i)
            border = center + step
            continue
        if cur_direction != next_dirction:
            cur_direction = next_dirction

        cur_direction, next_dirction, point, step, border = direction(point, cur_direction, step, border)
        set_value(point, matrix, i)

    return matrix


def generateMatrix2(n):
    """
    从顶点开始生成顺时针旋转矩阵
    :param n:
    :return:
    """
    l = 0
    r = n - 1
    t = 0
    b = n - 1
    num = 0
    tar = n * n
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    while num <= tar:
        for i in range(l, r + 1):
            num += 1
            matrix[t][i] = num
        t += 1
        for i in range(t, b + 1):
            num += 1
            matrix[i][r] = num
        r -= 1
        for i in range(r + 1, l - 1, -1):
            num += 1
            matrix[b][i] = num
        b -= 1
        for i in range(b + 1, t - 1, -1):
            num += 1
            matrix[i][l] = num
        l += 1
    return matrix


def count_paths(m, n):
    results = [[1 for i in range(n)] for i in range(m)]
    for i in range(1, n):
        for j in range(1, m):
            results[j][i] = results[j - 1][i] + results[j][i - 1]
    print(results)
    return results[-1][-1]


def waysToStep(n: int) -> int:
    res = [0 for _ in range(n + 1)]
    res[0] = 1
    for i in range(1, n + 1):
        res[i] = res[i - 1]
        if i >= 2:
            res[i] = (res[i] + res[i - 2]) % 1000000007
        if i >= 3:
            res[i] = (res[i] + res[i - 3]) % 1000000007
    print(res)
    return res[-1]


def calculate_area(matrix):
    n = len(matrix)
    res = [[0 for _ in range(n)] for _ in range(n)]
    area = 0
    j = i = 0
    width = height = 0

    for i in range(1, n):
        for j in range(i, n):
            pass

    while i < n:
        i0 = i
        j0 = j = 0
        width = height = 0
        while j < n:
            if matrix[i][j] == 1:
                if width == 0 and height == 0:
                    width += 1
                    height += 1
                    j += 1

                if j - j0 > i - i0:
                    width += 1
                    i += 1

                if j - j0 < i - i0:
                    height += 1
                    j += 1

            break
        e = min(width, height)
        area = max(area, e * e)

        i = i0 + 1


def setZeroes(matrix):
    """
    https://leetcode-cn.com/problems/set-matrix-zeroes/
    将0所在的行列设置为0
    :param martix:
    :return:
    """
    n = len(matrix)
    m = len(matrix[0])
    res = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                res.append((i, j))

    for i, j in res:
        for x in range(n):
            matrix[x][j] = 0

        for y in range(m):
            matrix[i][y] = 0


def generateTriangle(num):
    """
    杨辉三角
    :param num:
    :return:
    """


def queen8():
    """
    八皇后问题
    :return:
    """


def print_matrix(matrix):
    """
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
    :param matrix:
    :return:
    """


def mostPointsLine(points):
    """
    给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
    :param points:
    :return:
    """


import pprint

m = [[1, 2], [3, 4]]
# pprint.pprint(m)
# rotate(m)
# res = spiralOrder(m)
# res = generateMatrix(6)
# res = generateMatrix2(6)
# res = count_paths(6,5)
res = waysToStep(4)
pprint.pprint(res)
