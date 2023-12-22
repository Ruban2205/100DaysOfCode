# Implementation of Stack Data Structure
print("\nRuban Gino Singh - Day 87 of #100DaysOfCode\n")

print("Python program to Implement Stack Data Structure\n")

class Stack: 
    def __init__(self): 
        self.stack = list()
        self.maxsize = 10
        self.top = -1

    def push(self, data): 
        if self.top == self.maxsize - 1: 
            print("Stack is Full")
        else: 
            self.top += 1
            self.stack.append(data)

    def pop(self):
        if self.top == -1: 
            print("Stack is EMPTY!!")
        else:
            item = self.stack.pop()
            self.top = -1
            print("Deleted item is: ", item)

    def display(self): 
        print(self.stack)

Obj = Stack()
while(True): 
    print("\n1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    print("4. EXIT")

    choice = int(input("Enter your choice: "))
    if(choice == 1):
        value = int(input("Enter the data: "))
        Obj.push(value)
    
    elif choice == 2: 
        Obj.pop()

    elif choice == 3: 
        Obj.display()
    
    else: 
        break

# --------------------------------------------------------- #