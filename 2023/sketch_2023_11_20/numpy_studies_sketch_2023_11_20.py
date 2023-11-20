import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[7, 8], [9, 10], [11, 12]])
c = np.array([[13, 14], [15, 16], [17, 18]])

triangles = np.concatenate((a, b, c), axis=1).reshape(-1, 2)
triangles2 = np.hstack((a, b, c)).reshape(-1, 2)

print(triangles)
print(triangles2)
