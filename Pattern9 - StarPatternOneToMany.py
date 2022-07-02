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

if __name__ == '__main__':
    pattern9()