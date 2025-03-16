def pascal_triangle(n):
    triangle = [[1],[1,1]]
    for i in range(2, n+1):
        row = [1]
        for j in range(1, i):
            row.append(int(triangle[i-1][j-1]) + int(triangle[i-1][j]))
        row.append(1)
        triangle.append(row)
    for row in triangle:
        print(' '.join(map(str, row)))

pascal_triangle(6)