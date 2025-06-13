# Program 1
# Swap two numbers

a = int(input("A: "))
b = int(input("B: "))
print(f"Before swap:\na:{a}\tb:{b}")
c = a
a = b
b = c
print(f"After swap:\na:{a}\tb:{b}")

# Program 2
# Swap two numbers - Using + and -

a = int(input("A: ")) # a = 10
b = int(input("B: ")) # b = 20
print(f"Before swap:\na:{a}\tb:{b}")
a = a + b # a = 10 + 20 = 30
b = a - b # b = 30 - 20 = 10
a = a - b # a = 30 - 10 = 20
print(f"After swap:\na:{a}\tb:{b}")

# Program 3
# Swap two numbers - Using * and floor division (//)

a = int(input("A: ")) # a = 10
b = int(input("B: ")) # b = 20
print(f"Before swap:\na:{a}\tb:{b}")
a = a + b 
b = a // b 
a = a // b 
print(f"After swap:\na:{a}\tb:{b}")
