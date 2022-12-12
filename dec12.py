import numpy as np

with open('data12.txt') as f:
    input = f.read()
rows = input.split('\n')
M=len(rows)
N=len(rows[0])

scores = -np.ones((M,N))
moves =  np.chararray((M, N))
moves[:] = '.'

for i in range(M):
    for j in range(N):
        if rows[i][j]=='S':
            scores[i,j] = 0
            break


for i in range(M):
    for j in range(N):
        if rows[i][j]=='S':
            scores[i,j] = 0
            break



print('hej')


