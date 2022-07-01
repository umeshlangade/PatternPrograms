# PATTERN STYLE

# 333
# 222
# 111

row = int(input('Kindly provide row limit : '))
col = int(input('Kindly provide col limit : '))

row += 1
col += 1

for i in range(row, 0, -1):
    for j in range(col, 0, -1):
        # print(f 'row-{i} column-{j}')
        print(f'{i}', end="")
    print()


# REVERSE LOOP LOGIC
# for i in range(row,-1,-1):
#     print(f 'row {i}')
