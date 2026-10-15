# num1 and num2 variables are the global variable
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

def calculate_sum():
    global num1, num2
    sum3 = (num1 + num2) # This is a local variable
    print (f"Sum: {sum3}")


def calculate_difference():
    global num1, num2
    diff = num1 - num2 # This is another local variable
    print(f"Difference: {diff}")

calculate_sum()
calculate_difference()



