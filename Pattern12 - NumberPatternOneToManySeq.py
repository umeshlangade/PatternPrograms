# PATTERN STYLE

# A
# BB
# CCC
def char_pattern():
    row = int(input('Kindly provide row limit : '))
    row += 1
    col = row

    for i in range(1, row):
        for j in range(1,i):
            print(f'{chr(64+j)}', end="")
        print()


if __name__ == "__main__":
    char_pattern()