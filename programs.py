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
# Swap two numbers - Using * and floor division (//) - Except 0

a = int(input("A: ")) # a = 10
b = int(input("B: ")) # b = 20
print(f"Before swap:\na:{a}\tb:{b}")
a = a + b 
b = a // b 
a = a // b 
print(f"After swap:\na:{a}\tb:{b}")

# Program 4
# Swap two numbers - Using XOR (Only for integers)

a = int(input("A: ")) # a = 3
b = int(input("B: ")) # b = 4
print(f"Before swap:\na:{a}\tb:{b}")
a = a ^ b # 3-> 0011 4-> 0100 a = 3^4 = 7
b = a ^ b # 7-> 0111 4-> 0100 b = 7^4 = 3
a = a ^ b # 3-> 0011 7-> 0111 a = 3^7 = 4
print(f"After swap:\na:{a}\tb:{b}")

# Program 5
# Swap two numbers - packing and unpacking

a = int(input("A: ")) # a = 3
b = int(input("B: ")) # b = 4
print(f"Before swap:\na:{a}\tb:{b}")
a, b = b, a
print(f"After swap:\na:{a}\tb:{b}")

# Program 6
# Swap three numbers - Using temp variable

a = int(input("A: ")) 
b = int(input("B: ")) 
c = int(input("C: "))
d = a
a = c
c = b
b = d
print(f"a: {a}\tb:{b}\tc: {c}")

# Program 7
# Swap three numbers - Using + and -

a = int(input("A: ")) # 10
b = int(input("B: ")) # 20
c = int(input("C: ")) # 30
a = a + b + c #60
b = a - (b+c) # 60 - (50) = 10
c = a - (b+c) # 60 - (40) = 20
a = a - (b+c) # 60 - (30) = 30
# a = a + b + c
# b = a - b - c
# c = a - b - c
# a = a - b - c
print(f"a: {a}\tb:{b}\tc: {c}")

# Program 8
# Swap three numbers - Using * and /

a = int(input("A: ")) # 10
b = int(input("B: ")) # 20
c = int(input("C: ")) # 30
a = a * b * c
b = a // (b * c)
c = a // (b * c)
a = a // (b * c)
print(f"a: {a}\tb:{b}\tc: {c}")

# Program 9
# Swap three numbers - Using XOR

a = int(input("A: ")) # 10
b = int(input("B: ")) # 20
c = int(input("C: ")) # 30
a = a ^ b ^ c
b = a ^ b ^ c
c = a ^ b ^ c
a = a ^ b ^ c
print(f"a: {a}\tb:{b}\tc: {c}")
