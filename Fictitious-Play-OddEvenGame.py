import numpy as np

MAX_ITERATION = 1000000

pay_matrix = np.array([[-2, 3], [3, -4]])
pay_row = np.array([0, 0])
pay_column = np.array([0, 0])
action_one = 0
action_two = 0

def get_max(matrix):
    if matrix[0] >= matrix[1]:
        return 0
    else:
        return 1

def get_min(matrix):
    if matrix[0] >= matrix[1]:
        return 1
    else:
        return 0

for i in range(MAX_ITERATION):
    pay_column += pay_matrix[:][action_two]
    action_one = get_max(pay_column)
    pay_row += pay_matrix[action_one]
    action_two = get_min(pay_row)

print(pay_row/MAX_ITERATION)
print(pay_column/MAX_ITERATION)


