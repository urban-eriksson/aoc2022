with open('data13.txt') as f:
    input = f.read()

pairs = input.split('\n\n')


def compare_items(left_array, right_array):
    for left_value, right_value in zip(left_array, right_array):
        left_is_int = isinstance(left_value, int)
        right_is_int = isinstance(right_value, int)
        if left_is_int and right_is_int:
            if left_value < right_value:
                return 'correct'
            elif left_value > right_value:
                return 'incorrect'
        elif left_is_int:
            result = compare_items([left_value], right_value)
            if result != 'continue':
                return result
        elif right_is_int:
            result = compare_items(left_value, [right_value])
            if result != 'continue':
                return result
        else:
            result = compare_items(left_value, right_value)
            if result != 'continue':
                return result

    if len(left_array) < len(right_array):
        return 'correct'
    elif len(right_array) < len(left_array):
        return 'incorrect'
    else:
        return 'continue'


correct_indexes = []
for i, pair in enumerate(pairs, 1):
    left, right = (eval(s) for s in pair.split('\n'))
    result = compare_items(left, right)
    if result == 'correct':
        correct_indexes.append(i)
    elif result == 'continue':
        print('something wrong!')

print(f'Part1: {sum(correct_indexes)}')

all_packets = [eval(s) for pair in pairs for s in pair.split('\n')]
all_packets.append([[2]])
all_packets.append([[6]])
sorted_list = []
for left in all_packets:
    print(left)
    for i, right in enumerate(sorted_list):
        if compare_items(left, right) == 'correct':
            sorted_list.insert(i, left)
            break
    if i == len(sorted_list)-1 or len(sorted_list) == 0:
        sorted_list.append(left)

print(f'Part2: {(sorted_list.index([[2]])+1) * (sorted_list.index([[6]])+1)}')
