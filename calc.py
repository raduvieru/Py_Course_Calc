def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    pass


def division(x, y):
    pass


def floordivision(x, y):
    pass


def modulus(x, y):
    pass


def exponent(x, y):
    pass

while True:
    op = input('Calculator. Press operation key:\n"+" - Addition\n"-" - Subtraction\n"*" - Multiplication\n"/" - Division\n"//" - Floor Division\n"%" - Modulus\n"**" - Exponent\n...or any other key for break operation\n')
    operators = ['+', '-', '*', '/', '//', '%', '**']
    if op not in operators:
        break
    print("Input values for:")
    try:
        a = int(input("A = "))
        b = int(input("B = "))
    except:
        print("Sorry, invalid number!!!")
        input()
        continue
    if op == '+':
        print("A + B = ", addition(a, b))
        input()
    elif op == '-':
        print("A - B = ", subtraction(a, b))
        input()
    elif op == '*':
        print("A * B =")
        input()
    elif op == '/':
        print("A / B =")
        input()
    elif op == '//':
        print("A / B =")
        input()
    elif op == '%':
        print("A % B =")
        input()
    elif op == '**':
        print("A ** B =")
        input()