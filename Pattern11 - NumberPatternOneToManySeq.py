# PATTERN STYLE

# 1
# 12
# 123
# 1234

row = int(input('Kindly provide row limit : '))
row += 1
col = row

for i in range (1,row):
    for j in range(1, i):
        print(f'{j}',end="")
    print()

