'''
ADVANCED CALCULATOR 
'''

# import math

# class Basiccalculator:
#     def add(self, x, y): return x + y
#     def subtract(x, y): return x - y
#     def multiply(x, y): return x * y
#     def divide(x, y): return x / y if y != 0 else "Error"
#     def calculator():
#         while True:
#             choice = input("Enter operator (+,-,*,/) or 'exit': ")
#             if choice.lower() == 'exit': break
#             if choice in ('Sum', 'Sub', 'Multiply', 'Divide'):
#                 try:
#                     n1, n2 = int(input("Num 1: ")), int(input("Num 2: "))
#                     if choice == 'Sum': print(add(n1, n2))
#                     elif choice == 'Sub': print(subtract(n1, n2))
#                     elif choice == 'Multiply': print(multiply(n1, n2))
#                     elif choice == 'Divide' : print(divide(n1, n2))

#                 except ValueError: print("Invalid number")
#             else: print("Invalid operator")

#     calculator()


# class Advancedcalculator:
#     def calculator():
#         print("--- Advanced Calculator ---")
#         print("1. Power (x^y)      2. Square Root (√x)   3. Logarithm (log)")
#         print("4. Sine (sin)       5. Cosine (cos)       6. Tangent (tan)")
#         print("7. Factorial (x!)   8. Exit")
        
#         while True:
#             choice = input("Choose an option (1-8): ")
#             if choice == '8': 
#                 print("Goodbye!")
#                 break
                
#             if choice not in ('1', '2', '3', '4', '5', '6', '7', '+', '-', '*','/'):
#                 print("Invalid choice!")
#                 continue
                
#             try:
#                 # Power and Logarithm require two numbers
#                 if choice in ('1', '3'):
#                     x = float(input("Enter first number: "))
#                     y = float(input("Enter second number (exponent/base): "))
                    
#                     if choice == '1':
#                         print("Result:", math.pow(x, y))
#                     elif choice == '3':
#                         # math.log(x, base)
#                         print("Result:", math.log(x, y) if x > 0 and y > 1 else "Error: Invalid log bounds")
                
#                 # Factorial requires an integer
#                 elif choice == '7':
#                     x = int(input("Enter a positive integer: "))
#                     print("Result:", math.factorial(x))
                    
#                 # Trigonometry and Square Root require one number
#                 else:
#                     x = float(input("Enter number: "))
#                     if choice == '2':
#                         print("Result:", math.sqrt(x) if x >= 0 else "Error: Negative square root")
#                     elif choice == '4':
#                         print("Result (sin):", math.sin(math.radians(x)))
#                     elif choice == '5':
#                         print("Result (cos):", math.cos(math.radians(x)))
#                     elif choice == '6':
#                         print("Result (tan):", math.tan(math.radians(x)))
                        
#             except ValueError:
#                 print("Error: Invalid numerical input!")
#             except OverflowError:
#                 print("Error: Number too large!")

#     calculator()








import math


class BasicCalculator:

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

    def calculator(self):

        while True:

            print("\n----- BASIC CALCULATOR -----")
            print("+  Addition")
            print("-  Subtraction")
            print("*  Multiplication")
            print("/  Division")
            print("0  Exit")

            choice = input("Enter choice: ")

            if choice == "0":
                break

            if choice in ("+", "-", "*", "/"):

                try:
                    x = int(input("Enter first number: "))
                    y = int(input("Enter second number: "))

                    if choice == "+":
                        print("Result:", self.add(x, y))

                    elif choice == "-":
                        print("Result:", self.subtract(x, y))

                    elif choice == "*":
                        print("Result:", self.multiply(x, y))

                    elif choice == "/":
                        print("Result:", self.divide(x, y))

                except ValueError:
                    print("Invalid Input!")

            else:
                print("Invalid Choice!")


class AdvancedCalculator(BasicCalculator):

    def power(self, x, y):
        return math.pow(x, y)

    def square_root(self, x):
        return math.sqrt(x)

    def logarithm(self, x, base):
        return math.log(x, base)

    def sine(self, x):
        return math.sin(math.radians(x))

    def cosine(self, x):
        return math.cos(math.radians(x))

    def tangent(self, x):
        return math.tan(math.radians(x))

    def factorial(self, x):
        return math.factorial(x)

    def calculator(self):

        while True:

            print("\n----- ADVANCED CALCULATOR -----")
            print("1. Power")
            print("2. Square Root")
            print("3. Logarithm")
            print("4. Sine")
            print("5. Cosine")
            print("6. Tangent")
            print("7. Factorial")
            print("8. addition")
            print("9. subtract")
            print("10. divide")
            print("11. multiply")
            print("12. Exit")

            choice = input("Enter choice: ")

            try:

                if choice == "1":
                    x = int(input("Enter number: "))
                    y = int(input("Enter power: "))
                    print("Result:", int(self.power(x, y)))

                elif choice == "2":
                    x = int(input("Enter number: "))

                    if x < 0:
                        print("Negative number not allowed")
                    else:
                        print("Result:", int(self.square_root(x)))

                elif choice == "3":
                    x = float(input("Enter number: "))
                    base = float(input("Enter base: "))

                    if x <= 0 or base <= 0 or base == 1:
                        print("Invalid logarithm values")
                    else:
                        print("Result:", int(self.logarithm(x, base)))

                elif choice == "4":
                    x = float(input("Enter angle in degrees: "))
                    print("Result:", int(self.sine(x)))

                elif choice == "5":
                    x = float(input("Enter angle in degrees: "))
                    print("Result:", int(self.cosine(x)))

                elif choice == "6":
                    x = float(input("Enter angle in degrees: "))
                    print("Result:", int(self.tangent(x)))

                elif choice == "7":
                    x = int(input("Enter integer: "))

                    if x < 0:
                        print("Factorial not defined")
                    else:
                        print("Result:", self.factorial(x))

                elif choice == "8":
                     print("Result", self.add(x, y))

                elif choice == "9":
                     print("Result:", self.subtract(x, y))

                elif choice == "10":
                    print("Result:", self.divide(x, y))

                elif choice == "11":
                     print("Result:", self.multiply(x, y))

                elif choice == "12":
                    break

                else:
                    print("Invalid Choice!")

            except ValueError:
                print("Invalid Input!")

            except OverflowError:
                print("Number too large!")

while True:

    print("\n========== CALCULATOR ==========")
    print("1. Basic Calculator")
    print("2. Advanced Calculator")
    print("3. Exit")

    mode = input("Choose mode: ")

    if mode == "1":
        basic = BasicCalculator()
        basic.calculator()

    elif mode == "2":
        advanced = AdvancedCalculator()
        advanced.calculator()

    elif mode == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")