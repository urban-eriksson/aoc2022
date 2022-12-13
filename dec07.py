input=''''''


test_sum=0
for s in input.split('\n'):
    s0 = s.split(' ')[0]
    if s0.isdigit():
        test_sum += int(s0)


def get_sub_dirs(rows):
    sub_root = {}
    while rows:
        row = rows.pop(0)
        if row == ('$ cd ..'):
            return sub_root, rows
        elif row.startswith('$ cd'):
            name = row.split(' ')[2]
            sub_root[name]['content'], rows = get_sub_dirs(rows[1:])
        elif row.startswith('dir'):
            name = row.split(' ')[1]
            sub_root[name] = {'type': 'dir', 'content': {}}
        else:           
            size, name = row.split(' ')
            sub_root[name] = {'type':'file', 'size': int(size)}
    return sub_root, []

def get_sub_dirs2(rows):
    res = []
    while rows:
        row = rows.pop(0)
        if row == ('$ cd ..'):
            return res, rows
        elif row.startswith('$ cd'):
            sub_res, rows = get_sub_dirs2(rows[1:])
            res.append(sub_res)
        elif row.startswith('dir'):
            pass
        else:           
            size, _ = row.split(' ')
            res.append(int(size))
    return res, rows    

root,_ = get_sub_dirs2(input.split('\n')[2:])

def unpack_all_sizes(root):
    size = 0
    sizes = []
    for item in root:
        if type(item) == int:
            size += item
        else:
            sub_sizes, sub_size = unpack_all_sizes(item)
            sizes.extend(sub_sizes)
            size += sub_size
    sizes.append(size)
    return sizes, size



#46233734
# 23766266
# 6233734
size_list,size = unpack_all_sizes(root)

print('hej')