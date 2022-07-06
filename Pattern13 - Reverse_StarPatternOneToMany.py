# PATTERN STYLE

# *****
# ****
# ***
# **
# *

def pattern13():
    row = int(input('Kindly provide row limit : '))
    row += 1
    col = row
    for i in range(1, row+1):
        for j in range(1,row+2-i):
            print("*", end=" ")
        print()

if __name__ == '__main__':
    pattern13()