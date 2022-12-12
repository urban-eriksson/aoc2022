def process_neighbors(i,j,rows,moves,scores):
    score0 = scores[i][j]
    if i>0 and moves[i-1][j] == '.' and ord(rows[i][j]) - ord(rows[i-1][j]) <= 1:
        moves[i-1][j] = 'v'
        scores[i-1][j] = score0 + 1
    if i<M-1 and moves[i+1][j] == '.' and ord(rows[i][j]) - ord(rows[i+1][j]) <= 1:
        moves[i+1][j] = '^'
        scores[i+1][j] = score0 + 1
    if j>0 and moves[i][j-1] == '.' and ord(rows[i][j]) - ord(rows[i][j-1]) <= 1:
        moves[i][j-1] = '>'
        scores[i][j-1] = score0 + 1
    if j<N-1 and moves[i][j+1] == '.' and ord(rows[i][j]) - ord(rows[i][j+1]) <= 1:
        moves[i][j+1] = '<'
        scores[i][j+1] = score0 + 1

with open('data12.txt') as f:
    input = f.read()

rows = input.split('\n')
M=len(rows)
N=len(rows[0])

moves = []
scores = []
for _ in range(M):
    moves.append(['.']*N)
    scores.append([0]*N)

for i in range(M):
    for j in range(N):
        if rows[i][j]=='E':
            rows[i] = rows[i].replace('E', '{')
            moves[i][j]='*'
            process_neighbors(i,j,rows,moves,scores)
        if rows[i][j]=='S':
            rows[i] = rows[i].replace('S','`')

while scores[20][0] == 0:
    for i in range(M):
        for j in range(N):
            if moves[i][j] != '.':
                process_neighbors(i,j,rows,moves,scores)

print(f'Part1: {scores[20][0]}')

a_scores = []
for i in range(M):
    for j in range(N):
        if rows[i][j]=='a' and scores[i][j] != 0:
            a_scores.append(scores[i][j])

print(f'Part2: {min(a_scores)}')
