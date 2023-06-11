def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


OPERATIONS = {
    '+': add,
    '-': sub,
    '*': multiply,
    '/': division
}


def calculate(n1, n2, op):
    return OPERATIONS[op](n1=n1, n2=n2)


n1 = int(input("Pick the first number: "))
n2 = int(input("Pick the second number: "))
op = input("Chose the operation: ")

result = calculate(n1, n2, op)

print(f"The result is {result}.")
