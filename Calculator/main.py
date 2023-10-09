from art import logo
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multipy(n1,n2):
    return n1*n2

def devide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-":subtract,
    "*":multipy,
    "/":devide,
}

def calculator():
    print(logo)
    should_finished = False
    num1 = float(input("What's your first number?:"))

    while not should_finished:
        for operators in operations:
            print(operators)   
        operation_Symbol = input("Pick an operation:")   
        num2 = float(input("What's your next number?:"))       
        calculation_Function = operations[operation_Symbol] 
        answer = calculation_Function(num1,num2)
        print(f"{num1} {operation_Symbol} {num2} = {answer}")
        call_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation : ") 
        if call_again == 'y':
            should_finished = False
            num1 = answer
        else:
            should_finished == True 
            calculator()
        
   
calculator()
