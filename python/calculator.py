#building my calculator
#setting up the first set of dicts to establish the functions i want to perform later
def add(x,y):
    return x+y
def subtract(x,y): #something that i'd really like to implement are optimal writing conventions
    return x-y #should there be spaces between integers and operators?
def multiply(x,y):
    return x*y #easier for me to see.. but maybe it's unnecessary space?
def divide(x,y):
    #what if y = 0..
    if y == 0:
        return "Undefined (can not divide by zero)"
    return x/y 
def power(x,y):
    return x**y
def square_root(x):
    x ** 0.5 #this is effectively x to the power of 1/2 which is sqrt(x)

history = []

def main():
    while True:
        print("\nOptions:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'power' to raise to a power")
        print("Enter 'sqrt' for square root")
        print("Enter 'history' to see the calculation history")
        print("Enter 'quit' to end the program")

        user_input = input(": ")

        if user_input == "quit": #these are basically conditional statements
            break
        elif user_input == "history":
            for item in history:
                print(item)
            continue 

        #for operations requiring two numbers
        if user_input in ["add","subtract","multiply","divide","power"]:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            if user_input=="add":
                result=add(x,y)
                history.append(f"{x}+{y}={result}")
            elif user_input=="subtract":
                result=subtract(x,y)
                history.append(f"{x}-{y}={result}")
        #for square root
        elif user_input=="sqrt":
            x = float(input("Enter number for square root: "))
            result = square_root(x)
            history.append(f"sqrt({x})={result}")
        print(f"Result: {result}")

if __name__ == "__main__":
    main()