import numpy as np

# array = np.array([1,2,3,4])
# array *= 2
# print(array)

# ===================================================================
# ================================= NUMPY ===========================
# ===================================================================

# ==================== Diemensions Of Arrays ====================

# array = np.array([[["A", "B", "C"], ["A", "B", "C"], ["A", "B", "C"]], [
#                  ["A", "B", "C"], ["A", "B", "C"], ["A", "B", "C"]]])
# print("diemension", array.ndim)
# print("value", array)
# print("Shape", array.shape)


# ==================== Arrays Slicing ====================

# array = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
#array[start:end:step]
# print(array[:: -2])
# print(array[:, 2])
# print(array[::])


# ==================== Broadcasting Arrays ====================

# array1 = np.array([[1, 2, 3, 4]])
# array2 = np.array([[1], [2], [3], [4]])

# print(array1.shape, array2.shape)
# print(array1 * array2)

# ==================== Summarizing Data ====================

# array = np.array([[1,2,3,4,5], [6, 7, 8, 9, 10]])
# array = np.array([1,2,3,4,5])

# print(np.sum(array))
# print(np.mean(array))
# print(np.average(array))

# ==================== Filtering Data ====================

ages = np.array([[14, 15, 22, 99, 42, 66, 78, 43, 29, 37, 51, 24, 11, 8]])

# teenage = ages[ages < 18]
# adults = ages[(ages >= 18) & (ages < 65)]
# seniors = ages[ages > 65]
# evens = ages[ages % 2 == 0]
# odds = ages[ages % 2 != 0]

# print(evens, odds)

# To preserve array in its actual form:

# adults = np.where(ages > 18, ages ,0)
# print(adults)

# ==================== Filtering Data ====================


