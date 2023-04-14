# Arithmetic Operation
num1 = 10
num2 = 20

sum_1 = num1 + num2

sum_2 = num1.__add__(num2)

sub = num1.__sub__(num2)

mul = num1.__mul__(num2)

div = num1.__truediv__(num2)  # /

floor_div = num1.__floordiv__(num2)  # //

print(sum_2)
print(sub)
print(mul)
print(div)
print(floor_div)

print(num1.__mod__(num2))
print(num1.__pow__(2))

a = True
b = False


print(a.__and__(b))
print(a.__or__(b))

print(num1.__le__(num2))
print(num1.__lt__(num2))

print(num1.__ge__(num2))
print(num1.__gt__(num2))

print(num1.__eq__(num2))
print(num1.__ne__(num2))

lst = [1,2,3,4,5,6]

print(lst.__contains__(5))