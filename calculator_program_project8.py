import os

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return None
    
operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    number1=float(input("Enter first number:"))
    for symbols in operations_dict:
        print(symbols)

    continue_flag=True
    while continue_flag:
        operation_symbol=input("Pick an operation:")
        number2=float(input("Enter second number:"))
        calculator_function=operations_dict[operation_symbol]
        output=calculator_function(number1,number2)
        print(f"{number1}{operation_symbol}{number2}={output}")
        should_continue=input(f"enter 'y' to continue calculation with {output} or 'n' to start new calculation or 'x' to exit:").lower()

        if should_continue=='y':
            number1=output
        elif should_continue=='n':
            continue_flag=False
            os.system("cls")
            calculator()
        else:
            continue_flag=False
            print("Bye!")
calculator()