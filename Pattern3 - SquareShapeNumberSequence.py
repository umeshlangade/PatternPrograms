# PATTERN STYLE

# 123
# 123
# 123

row = int(input('Kindly provide row limit : '))
col = int(input('Kindly provide col limit : '))

row += 1
col += 1

for i in range (1,row):
    for j in range(1,col):
        # print(f'row-{i} column-{j}')
        print(f'{j}',end="")
    print()