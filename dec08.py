with open('data08.txt') as f:
    input = f.read()

rows = input.split('\n')


def is_visible(h0, i, j, rows, direction):
    if i == 0 or j == 0 or i == len(rows)-1 or j == len(rows[i])-1:
        return True
    elif direction == 'N':
        return h0 > rows[i-1][j] and is_visible(h0, i-1, j, rows, 'N')
    elif direction == 'E':
        return h0 > rows[i][j+1] and is_visible(h0, i, j+1, rows, 'E')
    elif direction == 'S':
        return h0 > rows[i+1][j] and is_visible(h0, i+1, j, rows, 'S')
    elif direction == 'W':
        return h0 > rows[i][j-1] and is_visible(h0, i, j-1, rows, 'W')


part1 = sum([is_visible(rows[i][j], i, j, rows, 'N') or is_visible(rows[i][j], i, j, rows, 'E') or is_visible(
    rows[i][j], i, j, rows, 'S') or is_visible(rows[i][j], i, j, rows, 'W') for i in range(len(rows)) for j in range(len(rows[0]))])

print(f'Part1: {part1}')

def scenic_length(h0, i, j, rows, direction, acc, init):
    if i == 0 or j == 0 or i == len(rows)-1 or j == len(rows[i])-1 or (rows[i][j] >= h0 and not init):
        return acc
    elif direction == 'N':
        return scenic_length(h0, i-1, j, rows, 'N', acc+1, False)
    elif direction == 'E':
        return scenic_length(h0, i, j+1, rows, 'E', acc+1, False)
    elif direction == 'S':
        return scenic_length(h0, i+1, j, rows, 'S', acc+1, False)
    elif direction == 'W':
        return scenic_length(h0, i, j-1, rows, 'W', acc+1, False)


part2 = max([scenic_length(rows[i][j], i, j, rows, 'N', 0, True) * scenic_length(rows[i][j], i, j, rows, 'E', 0, True) * scenic_length(rows[i]
            [j], i, j, rows, 'S', 0, True) * scenic_length(rows[i][j], i, j, rows, 'W', 0, True) for i in range(len(rows)) for j in range(len(rows[0]))])

print(f'Part2: {part2}')