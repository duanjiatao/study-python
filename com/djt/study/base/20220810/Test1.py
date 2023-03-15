import decimal
from fractions import Fraction

print("=================================")
a = 2.1E5
print(a)

print("=================================")
f3 = 0.0000000000000000000000000847
print("f3Value: ", f3)
print("f3Type: ", type(f3))

print("=================================")
print(0.1 + 0.2)
print(0.3 == (0.1 + 0.2))

print("=================================")
a = decimal.Decimal("10.0")
b = decimal.Decimal("3")
print(10.0 / 3)
print(a / b)

print("=================================")
print(10 / 3)
print(Fraction(10, 3))
