#! /usr/bin/env python3


def get_input():
    # get the input
    number = int(input("Enter the number: "))

    return number

def fibonacci(number):
    # intialize our variables for calculating the Fibonacci number at this position
    a,b = 0,1

    # one way to calculate the Fibonacci number
    for i in range(int(number)):
        a,b = b, a+number

    # store results so its obvious
    fibonacci_number = a

    return fibonacci_number

def print_fibonacci(number, fibonacci_number):
    # print the output
    print("The fibonacci number for", number, "is:", fibonacci_number)

def main():
    input_num = get_input()
    fibonacci_number = fibonacci(input_num)
    print_fibonacci(input_num, fibonacci_number)


if __name__ == '__main__':
    main()
