def check_float(floatA, floatB): #checks user inputted floaters
    """
    checks user inputted floatA and floatB
    declares num1, num2
    returns num1, num2
    if error returns None and prints
    """
    if floatA.strip().lower() == "exit" or floatB.strip().lower() == "exit":
        return "exit"
    try:
        num1 = float((floatA).strip())
        num2 = float((floatB).strip())
        return num1, num2
    except ValueError:
        print("Please enter numeric values and try again.")
        return None

def check_operator(operator): #checks user inputted operators
    """
    declares op_fixed
    checks user inputted operator via comparing with accepted operators
    returns op_fixed or False
    """
    op_fixed = operator.strip().lower()
    if op_fixed == '+' or op_fixed == '-' or op_fixed == '*' or op_fixed == '/':
        return op_fixed
    elif op_fixed.lower() == "exit":
        return "exit"
    print("Invalid operator. Please try again.")
    return None


def fancy_printer(num1, num2, operator, math_complete):
    """
    compares math_complete does not equal None prints if it does return None
    prints answer in a nice way
    """
    if math_complete != None:
        print("Equation: " + str(num1) + " " + operator + " " + str(num2) + " = " + str(math_complete))
    else:
        return None
def math_doer(num1, num2, operator):
    """
    declares math_complete
    checks if num2 is 0 and prints if it is
    does math via comparing operator, using num1, num2, and operator
    """
    if operator == '+':
        math_complete = (num1 + num2)
        return math_complete
    elif operator == '-':
        math_complete = (num1 - num2)
        return math_complete
    elif operator == '*':
        math_complete = (num1 * num2)
        return math_complete
    elif operator == '/':
        if num2 != 0:  # checks if num2 if 0
            math_complete = (num1 / num2)
            return math_complete
        else:
            print("Cannot divide by 0.")
            return None

    return None


def operator_input():
    """
    declares operator
    calls check_operator if true returns operator
    """
    while True:
        operator = input("Please enter operator(+, -, *, /) or type exit to exit program: ")
        op_fixed = check_operator(operator)
        if op_fixed != None:
            return op_fixed
def float_input():
    """
    declares float A, floatB, and good_float
    gets user input for two numbers
    calls check_float(floatA, floatB)
    returns good_float
    """
    while True:
        floatA = input("Enter a number: ")
        floatB = input("Enter another number:")
        good_float = check_float(floatA, floatB)
        if good_float != None:
            return good_float

def main():
    """
    declares num_exit_check, num1, num2, operator, math_complete
    loops unless user types exit
    calls float_input(), operator_input(), math_doer(), and fancy_printer()

    """
    print("Type Exit to exit the program.")
    while True:
        num_exit_check = float_input()
        if num_exit_check == "exit":
            print("Exiting program.")
            break
        num1, num2 = float_input()
        operator = operator_input()
        if operator == "exit": #exit program
            print("Exiting Program.")
            break
        math_complete = math_doer(num1, num2, operator)
        fancy_printer(num1, num2, operator, math_complete)

if __name__ == "__main__":
    main()
