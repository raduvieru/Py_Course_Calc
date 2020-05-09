def summary(x, y):
    return x + y


def decrement(x, y):
    return x - y


while True:
    op = input('Calculator. Press operation key:\n"+" - Addition\n"-" - Subtraction\n"*" - Multiplication\n"/" - Division\n"//" - Floor Division\n"%" - Modulus\n"**" - Exponent\n...or any other character for break operation\n')
    operators = ['+','-','/','//','%','**']
    if op not in operators:
        break
    print("Input values for:")
    a = int(input("A = "))
    b = int(input("B = "))
    if op == '+':
        print("A + B = ", summary(a, b))
    elif op == '-':
        print("A - B = ", decrement(a, b))
    elif op == '/':
        print("A / B =")
    elif op == '//':
        print("A / B =")



