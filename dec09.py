def get_distance(H, T):
    return ((H[0]-T[0])**2 + (H[1]-T[1])**2)**(1/2)


def update_tail_position(H, T):
    T = T[0] + min(max(H[0]-T[0], -1), 1), T[1] + min(max(H[1]-T[1], -1), 1)
    return T


with open('data09.txt') as f:
    input = f.read()

rows = input.split('\n')

H = (0, 0)
T = (0, 0)
visited = set()
visited.add(T)
for row in rows:
    direction, n = row.split()
    for _ in range(int(n)):
        if direction == 'U':
            H = (H[0], H[1] + 1)
        elif direction == 'R':
            H = (H[0] + 1, H[1])
        elif direction == 'D':
            H = (H[0], H[1] - 1)
        elif direction == 'L':
            H = (H[0] - 1, H[1])
        if get_distance(H, T) >= 2:
            T = update_tail_position(H, T)
            visited.add(T)

part1 = len(visited)
print(f'Part1: {part1}')

K = [(0, 0)]*10
visited = set()
visited.add(K[9])
for row in rows:
    direction, n = row.split()
    for _ in range(int(n)):
        if direction == 'U':
            K[0] = (K[0][0], K[0][1] + 1)
        elif direction == 'R':
            K[0] = (K[0][0] + 1, K[0][1])
        elif direction == 'D':
            K[0] = (K[0][0], K[0][1] - 1)
        elif direction == 'L':
            K[0] = (K[0][0] - 1, K[0][1])
        for i in range(9):
            if get_distance(K[i], K[i+1]) >= 2:
                K[i+1] = update_tail_position(K[i], K[i+1])
            else:
                break
            if i == 8:
                visited.add(K[9])

part2 = len(visited)
print(f'Part2: {part2}')
