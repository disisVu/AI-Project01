import numpy as np

m = np.zeros((3,3))
def vertical_matrix(matrix):
    matrix_temp = []
    for i in range(0, len(matrix)):
        matrix_temp.append(matrix[::-1][i])
    return matrix_temp

m[0][0] = 1 
m[1][1] = 2
m[2][2] = 1
print(m)

m2 = np.flipud(m)
m3 = np.diag(m2)
print(m2)
print(m3)
if all(m3 == 1):
    print("yes\n")
else:
    print("no")
