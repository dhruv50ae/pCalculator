# Calculator

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operationSymbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
calculationFunction = operations[operationSymbol]
answer = calculationFunction(num1, num2)

print(f"{num1} {operationSymbol} {num2} = {answer}")
