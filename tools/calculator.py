# Addition
# Subtraction
# Multiplication
# Division
# Exponent
# Factorial

while True:
    choice = int(input('''Enter the your choice:
    1] Addition
    2] Subtraction
    3] Multiplication
    4] Division
    5] Exponent
    6] Factorial
    '''))
    match choice:
        case 1:
            augend = int(input("Enter the augend: "))
            addend = int(input("Enter the addend: "))
            sum = augend + addend
            print('Sum: ', sum)
            break
        case 2:
            minuend = int(input("Enter the minuend: "))
            subtrahend = int(input("Enter the subtrahend: "))
            diff = minuend - subtrahend
            print('Difference: ', diff)
            break
        case 3:
            multiplicand = int(input("Enter the multiplicand: "))
            multiplier = int(input("Enter the multiplier: "))
            prod = multiplicand*multiplier
            print('Product: ', prod)
            break
        case 4:
            dividend = int(input("Enter the dividend: "))
            divisor = int(input("Enter the divisor: "))
            quotient = dividend/divisor
            print('Quotient: ', quotient)
            break
        case 5:
            base = int(input("Enter the base: "))
            exp = int(input("Enter the exponent: "))
            power = base**exp
            print('Power: ', power)
            break
        case 6:
            n = int(input("Enter the number: "))
            if n < 0 :
                print("Not valid for negative numbers")
            elif n == 0:
                print("Factorial: 1")
                break
            else: 
                fact = n
                for i in range(2, n):
                    fact *= i
                print("Factorial: ", fact)
                break
        case _:
            print("Invalid choice try again!")
