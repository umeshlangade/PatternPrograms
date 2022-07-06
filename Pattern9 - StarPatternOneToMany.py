# PATTERN STYLE

# *
# **
# ***
# ****
def pattern9():
    row = int(input('Kindly provide row limit : '))
    row += 1
    col = row
    for i in range(1, row):
        print('*'*i)


def pattern91():
    row = int(input('Kindly provide row limit : '))
    row += 1
    col = row

    for i in range(1,row+1):
        for j in range(1,i+1):
            print('*', end=" ")
        print()



if __name__ == '__main__':
    pattern9()
    # pattern91()