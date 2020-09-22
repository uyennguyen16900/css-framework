def rotate_array(a,n):
    remainder = len(a) % n
    temp = 0
    count = 1
    while count <= n:
        temp = a[-count]
        i = 0
        while i < len(a) // n - 1:
            a[-(i*n+count)] = a[-(i*n+n+count)]
            print(-(i*n+n+count))
            i+=1
        
        if remainder != 0:
            print(((i-1)*n+remainder+count+1), -((i-1)*n+remainder*2+count+1))
            a[-((i-1)*n+remainder+count+1)] = a[-((i-1)*n+remainder*2+count+1)]
        #     print(a)
        # else:
        #     a[-count+n] = temp

        count+=1
    







       
    return a
print(rotate_array([1,2,3,4,5,6,7,8], 3))
        
def rotate_matrix(matrix):
    n = len(matrix)
    for x in range(n // 2):
        for y in range(x, n - x - 1):
            temp = matrix[n-y-1][x]
            matrix[n-y-1][x] = matrix[n-x-1][n-y-1]
            matrix[n-x-1][n-y-1] = matrix[y][n-x-1]
            matrix[y][n-x-1] = matrix[x][y]
            matrix[x][y] = temp

    return matrix

matrix = [[1,2,3], [4,5,6,], [7,8,9]]
# print(rotate_matrix(matrix))