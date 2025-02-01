#Arithmetic oprators:
a = 13
b = 5
sum_result = a + b
diff_result = a - b
mul_result = a * b
div_result = a / b
mod_result = a % b
exp_result = a ** b
floor_result = a // b

print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", mul_result)
print("Division:", div_result)
print("Modulus:", mod_result)
print("Exponential:", exp_result)
print("Floor Division:", floor_result)


#Comparison operators:
a = 10
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#Logical operators:
a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)

#Assignment operators:
total = 10

#total += 5
#total -= 3
#total *= 2
#total /= 4
#total %= 5
#total **= 5
total //= 5

print(total)


#Bitwise operators:
a = 60
b = 13
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 2)
print(a >> 2)

#Identity operators & membership operators:
a = 10
b = 20
list = [10, 20, 30, 40, 50]
print(a is b)
print(a is not b)
print(a in list)
print(b not in list)
print(10 in list)
print(15 in list)


#Ternary operators:
a = 10
b = 20
min = a if a < b else b
print(min)
max = a if a > b else b
print(max)

#Operator precedence:
a = 10
b = 20
c = 30
d = 5
result = a + b * c / d
print(result)
result = (a + b) * c / d
print(result)
result = ((a + b) * c) / d
print(result)
result = (a + b) * (c / d)
print(result)
result = a + (b * c) / d
print(result)
result = a + b * (c / d)
print(result)
result = a + (b * c) / d
print(result)
result = a + b * c // d
print(result)
result = a + b * c % d
print(result)

 