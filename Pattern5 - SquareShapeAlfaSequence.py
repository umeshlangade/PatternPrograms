# PATTERN STYLE

# ABC
# ABC
# ABC

row = int(input('Kindly provide row limit : '))
col = int(input('Kindly provide col limit : '))

row += 1
col += 1
ascii_val = 64

for i in range(1, row):
    for j in range(1, col):
        # print(f 'row-{i} column-{j}')
        print(f'{chr(ascii_val+j)}', end="")
    print()
