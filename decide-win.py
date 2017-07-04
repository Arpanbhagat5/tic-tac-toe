matrix = [[2,1,1],[2,2,1],[0,1,2]]
winner = 0
for row in range(len(matrix)):
    if matrix[row][0] == matrix[row][1] and matrix[row][1] == matrix[row][2]:
        winner = matrix[row][0]

for col in range(len(matrix)):
    if matrix[0][col] == matrix[1][col] and matrix[1][col] == matrix[2][col]:
        winner = matrix[0][col]

if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
    winner = matrix[1][1]

if matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]:
    winner = matrix[1][1]

print winner
