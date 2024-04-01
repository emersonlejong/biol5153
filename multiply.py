#! usr/bin/env python3


def get_input():
    # ask for size of multiplication table
    size = int(input("Enter the size of your table: "))

    return size


def print_table(size):  

    # calculate how many spaces we will need for output of each cell in matrix
    cell_width = len(str((size * size))) + 1

    # nested for loop to calculate i * j
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            # nice formatted print statement for each cell
            print("{:>{cell_width}}".format(i * j, cell_width = cell_width), end = '')

        #print a newline character at the end of each row
        print()

def main():
    input_num = get_input()
    print_table(input_num)


if __name__ == '__main__':
    main()


