# Addition
# Subtraction
# Multiplication
# Division
# Exponent
# Factorial

def add(a, b):
    return a + b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    if b == 0:
        return "Divisor can't be Zero! Try Again."
    else:
        return a/b


def exponent(a, b):
    return a**b


def factorial(n):
    if n < 0:
        return "Not valid for negative numbers"
    elif n == 0:
        return "Factorial: 1"
    else:
        fact = n
        for i in range(2, n):
            fact *= i
        return f"Factorial: {fact}"


while True:
    choice = int(input('''Enter the your choice:
    1] Addition
    2] Subtraction
    3] Multiplication
    4] Division
    5] Exponent
    6] Factorial
    7] Quit
    '''))
    match choice:
        case 1:
            augend = int(input("Enter the augend: "))
            addend = int(input("Enter the addend: "))
            sum = add(augend, addend)
            print('Sum: ', sum)
        case 2:
            minuend = int(input("Enter the minuend: "))
            subtrahend = int(input("Enter the subtrahend: "))
            diff = subtract(minuend, subtrahend)
            print('Difference: ', diff)
        case 3:
            multiplicand = int(input("Enter the multiplicand: "))
            multiplier = int(input("Enter the multiplier: "))
            prod = multiply(multiplicand, multiplier)
            print('Product: ', prod)
        case 4:
            dividend = int(input("Enter the dividend: "))
            divisor = int(input("Enter the divisor: "))
            quotient = divide(dividend, divisor)
            print('Quotient: ', quotient)
        case 5:
            base = int(input("Enter the base: "))
            exp = int(input("Enter the exponent: "))
            power = exponent(base, exp)
            print('Power: ', power)
        case 6:
            n = int(input("Enter the number: "))
            print(factorial(n))
        case 7:
            break
        case _:
            print("Invalid choice try again!")
