import art

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculate():
    print(art.logo)
    num1 = float(input("Enter the first number: "))

    should_accumulate=True
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter the second number: "))
        answer=operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        decision=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: \n").lower()
        if decision =='y':
            num1=answer
        else:
            should_accumulate=False
            print("\n"*50)
            calculate()

calculate()