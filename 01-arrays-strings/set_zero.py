def set_zero(matrix):
    R, C = matrix.shape
    first_zero_row = False
    first_zero_col = False
    for c in range(C):
        if matrix[0, c] == 0:
            first_zero_row = True
            break
    for r in range(R):
        if matrix[0, r] == 0:
            first_zero_col = True
            break
    for r in range(1, R):
        for c in range(1, R):
            if matrix[r, c] == 0:
                matrix[0, c] = 0
                matrix[r, 0] = 0
    for c in range(C):
        if matrix[0, c] == 0:
            matrix[:, c] = 0
    for r in range(R):
        if matrix[r, 0] == 0:
            matrix[r,:] = 0
    if first_zero_row:
        matrix[0, :] = 0
    if first_zero_col:
        matrix[:, 0] = 0
    return matrix