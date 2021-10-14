
class Calculator: 
    # Constructor
    def __init__(self, input1, input2): 
        self.input1 = input1
        self.input2 = input2

    # Function for Addition
    def addition(self): 
        return self.input1 + self.input2

    # Function for Subtraction
    def subtraction(self): 
        return self.input1 - self.input2

    # Function for Multiplication
    def multiplication(self): 
        return self.input1 * self.input2

    # Function for Division
    def division(self): 
        return self.input1 / self.input2

# While loop to perform Menu Driven. 
while(True): 
    print("\nSimple Calculator")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. EXIT\n")

    choice = int(input("What do you want to perform?: "))

    if choice == 1: 
        value1 = int(input("Enter value1: "))
        value2 = int(input("Enter value2: "))

        # Object calling the Function
        calculator = Calculator(value1, value2)
        result = calculator.addition()
        print(result)

    elif choice == 2: 
        value1 = int(input("Enter value1: "))
        value2 = int(input("Enter value2: "))

        # Object calling the Function
        calculator = Calculator(value1, value2)
        result = calculator.subtraction()
        print(result)

    elif choice == 3: 
        value1 = int(input("Enter value1: "))
        value2 = int(input("Enter value2: "))

        # Object calling the Function
        calculator = Calculator(value1, value2)
        result = calculator.multiplication()
        print(result)

    elif choice == 4: 
        value1 = int(input("Enter value1: "))
        value2 = int(input("Enter value2: "))

        # Object calling the Function
        calculator = Calculator(value1, value2)
        result = calculator.division()
        print(result)

    elif choice == 5: 
        break

    else: 
        print("\nINVALID INPUT! Entered choice -> ", choice, " is NOT Available in the MENU!!")
