def toe(mat):
    # if not square matrix return false
    rows = len(mat)
    cols = len(mat[0])
    # if rows != cols:
    #     print("asdf")
    #     return False
    # # iterate
    for m in range(rows):
        for n in range(cols):
            # big diagonal is weird
            if n == 0 and m == 0:
                pass
            elif n == m and mat[n][m] != mat[0][0]:
                return False
            else:
                for i in range(rows-2):
                    if mat[n][m] != mat[n+i][m-i]:
                        print(n,m,i,n+i,m,mat[n][m],mat[n+i][m])
                 
                        return False
    print("Toe!")
    return True

mat = [[1,2,3,4,8], [5,1,2,3,4], [4,5,1,2,3], [7,4,5,1,2]]
toe(mat)