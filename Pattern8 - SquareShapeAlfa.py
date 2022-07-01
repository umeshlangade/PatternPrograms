# PATTERN STYLE

# JJJ
# III
# HHH

row = int(input('Kindly provide row limit : '))
col = int(input('Kindly provide col limit : '))

row += 1
col += 1
ascii_val = 74

for i in range(0, row):
    for j in range(0, col):
        # print(f 'row-{i} column-{j}')
        print(f'{chr(ascii_val-i)}', end="")
    print()


# REVERSE LOOP LOGIC
# for i in range(row,-1,-1):
#     print(f 'row {i}')
