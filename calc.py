def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    try:
        div = x / y
        return div
    except Exception as exc:
        return print("Error - ", exc)


def floor_div(x, y):
    try:
        div = x // y
        return div
    except Exception as exc:
        return print("Error - ", exc)


def modulus(x, y):
    try:
        div = x % y
        return div
    except Exception as exc:
        return print("Error - ", exc)


def exponent(x, y):
    return x ** y


if __name__ == "__main__":
    while True:
        op = input('Calculator. Press operation key:\n"+" - Addition\n"-" - Subtraction\n"*" - Multiplication\n"/" - '
                   'Division\n"//" - Floor Division\n"%" - Modulus\n"**" - Exponent\n...or any other key for break '
                   'operation\n')
        operators = ['+', '-', '*', '/', '//', '%', '**']
        if op not in operators:
            break
        print("Input values for:")
        try:
            a = int(input("A = "))
            b = int(input("B = "))
        except Exception as e:
            print("Error - ", e)
            input()
            continue
        if op == '+':
            print("A + B = ", addition(a, b))
            input()
        elif op == '-':
            print("A - B = ", subtraction(a, b))
            input()
        elif op == '*':
            print("A * B =", multiplication(a, b))
            input()
        elif op == '/':
            print("A / B =", division(a, b))
            input()
        elif op == '//':
            print("A // B =", floor_div(a, b))
            input()
        elif op == '%':
            print("A % B =", modulus(a, b))
            input()
        elif op == '**':
            print("A ** B =", exponent(a, b))
            input()
