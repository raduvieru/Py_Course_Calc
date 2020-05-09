def Addition(x, y):
    return x + y

def Subtraction(x, y):
    return x - y

def Multiplication(x, y):
    return x * y

def Division(x, y):
    try:
        div = x / y
        return div
    except:
        return print("Division by zero - error!")

def FloorDivision(x, y):
    try:
        div = x // y
        return div
    except:
        return print("Division by zero - error!")

def Modulus(x, y):
    try:
        div = x % y
        return div
    except:
        return print("Division by zero - error!")

def Exponent(x, y):
    return x ** y


while True:
    op = input('Calculator. Press operation key:\n"+" - Addition\n"-" - Subtraction\n"*" - Multiplication\n"/" - Division\n"//" - Floor Division\n"%" - Modulus\n"**" - Exponent\n...or any other key for break operation\n')
    operators = ['+', '-', '*', '/', '//', '%', '**']
    if op not in operators:
        break
    print("Input values for:",end='\n')
    a = int(input("A = "))
    b = int(input("B = "))
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
        print("A / B =", Division(a,b))
        input()
    elif op == '//':
        print("A / B =",FloorDivision(a,b))
        input()
    elif op == '%':
        print("A % B =",Modulus(a,b))
        input()
    elif op == '**':
        print("A ** B =",Exponent(a,b))
        input()