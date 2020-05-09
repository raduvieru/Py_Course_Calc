def Addition(x, y):
    return x + y


def Subtraction(x, y):
    return x - y

def Multiplication(x, y):
    pass

def Division(x, y):
    pass

def FloorDivision(x, y):
    pass

def Modulus(x, y):
    pass

def Exponent(x, y):
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
        print("A + B = ", Addition(a, b))
        input()
    elif op == '-':
        print("A - B = ", Subtraction(a, b))
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