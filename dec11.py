with open('data11.txt') as f:
    input = f.read()
chunks = input.split('\n\n')


def parse_monkey(chunk):
    rows = chunk.split('\n')
    items = [int(s.strip(',')) for s in rows[1].split('items:')[1].split()]
    parts = rows[2].split()
    if parts[4] == '*':
        if parts[5] == 'old':
            def operation(x): return x * x
        else:
            def operation(x): return x * int(parts[5])
    elif parts[4] == '+':
        def operation(x): return x + int(parts[5])

    def test(x): return int(rows[4].split(
    )[-1]) if x % int(rows[3].split()[-1]) == 0 else int(rows[5].split()[-1])
    denominator = int(rows[3].split()[-1])

    return {'items': items, 'operation': operation, 'test': test, 'count': 0, 'denominator': denominator}


monkeys = [parse_monkey(chunk) for chunk in chunks]

for i in range(20):
    for monkey in monkeys:
        while monkey['items']:
            item = monkey['items'].pop()
            worry_level = monkey['operation'](item)
            reduced_worry_level = worry_level // 3
            monkey_to = monkey['test'](reduced_worry_level)
            monkeys[monkey_to]['items'].append(reduced_worry_level)
            monkey['count'] += 1

sorted_monkeys = sorted(monkeys, key=lambda x: x['count'])

part1 = sorted_monkeys[-1]['count'] * sorted_monkeys[-2]['count']
print(f'Part1: {part1}')

monkeys = [parse_monkey(chunk) for chunk in chunks]

common_denominator = 1
for monkey in monkeys:
    common_denominator *= monkey['denominator']

for i in range(10000):
    for monkey in monkeys:
        while monkey['items']:
            item = monkey['items'].pop()
            worry_level = monkey['operation'](item)
            reduced_worry_level = worry_level % common_denominator
            monkey_to = monkey['test'](reduced_worry_level)
            monkeys[monkey_to]['items'].append(reduced_worry_level)
            monkey['count'] += 1

sorted_monkeys = sorted(monkeys, key=lambda x: x['count'])
part2 = sorted_monkeys[-1]['count'] * sorted_monkeys[-2]['count']
print(f'Part2: {part2}')
