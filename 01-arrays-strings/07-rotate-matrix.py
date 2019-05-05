'''
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?

[1,2,3,       [7,4,1,
 4,5,6,   ->   8,5,2,
 7,8,9]        9,6,3]

Time: O(n^2)
Space: O(1)
'''

import numpy as np

def rotate_matrix(matrix):
    # assume clockwise rotation
    N, M = matrix.shape
    assert(N == M)  # must be NxN matrix
    for l in range(N // 2):
        for i in range(l, N - 1 - l):
            # save first number from right column
            right_col_temp = matrix[i, - 1 - l]  
            
            # from top row to right column
            matrix[i, - 1 - l] = matrix[l, i]

            # from left column to top row
            matrix[l, i] = matrix[- 1 - i, l]

            # from bottom row to left column
            matrix[- 1 - i, l] = matrix[-1 - l, - 1 - i]

            # from right column to bottom row
            matrix[-1 - l, - 1 - i] = right_col_temp
    return matrix

# Test

if __name__ == '__main__':
    matrix = np.array([ [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9] ])
    print(matrix)
    print("    ||\n    \/")
    print(rotate_matrix(matrix))
    
    print()
    
    matrix = np.array([ [0, 1, 2, 3],
                        [4, 5, 6, 7],
                        [7, 8, 9, 'A'],
                    ['B', 'C', 'D', 'E'] ])
    print(matrix)
    print("\t||\n\t\/")
    print(rotate_matrix(matrix))