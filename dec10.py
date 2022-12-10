
with open('data10.txt') as f:
    input = f.read()
rows = input.split('\n')

X = 1
cycle = 1
signal = []

for i, row in enumerate(rows):
    instruction, *args = row.split()
    if instruction == 'addx':
        signal.append(cycle * X)
        cycle += 1
        signal.append(cycle * X)
        cycle += 1
        value = int(args[0])
        X += value
    elif instruction == 'noop':
        signal.append(cycle * X)
        cycle += 1

interesting = [20, 60, 100, 140, 180, 220]

part1 = sum([signal[i-1] for i in interesting])
print(f'Part1: {part1}')


class CRT:
    def __init__(self, width):
        self.width = width
        self.screen = []
        self.row = []

    def add_pixel(self, cycle, X):
        x_pos = cycle - self.width * len(self.screen)
        if x_pos - X >= 0 and x_pos - X < 3:
            c = '#'
        else:
            c = '.'
        self.row.append(c)
        if len(self.row) == self.width:
            self.screen.append(self.row)
            self.row = []

    def show(self):
        return ''.join([f"{''.join(v)}\n" for v in self.screen])


crt = CRT(width=40)
X = 1
cycle = 1
for i, row in enumerate(rows):
    instruction, *args = row.split()
    if instruction == 'addx':
        crt.add_pixel(cycle, X)
        cycle += 1
        crt.add_pixel(cycle, X)
        cycle += 1
        value = int(args[0])
        X += value
    elif instruction == 'noop':
        crt.add_pixel(cycle, X)
        cycle += 1

print(f'Part2: \n{crt.show()}')
