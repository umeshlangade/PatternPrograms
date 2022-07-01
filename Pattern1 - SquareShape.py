# PATTERN STYLE

# *****
# *****
# *****

row = int(input('Kindly provide row limit : '))
col = int(input('Kindly provide col limit : '))

for i in range (0,row):
    for j in range(0,col):
        # print(f'row-{i} column-{j}')
        print('*',end="")
    print()