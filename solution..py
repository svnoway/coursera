import sys

digit_string =sys.argv[1]
n = int(digit_string)
suma = 0
mult = 1
 
while n > 0:
    digit = n % 10
    suma = suma + digit
    mult = mult * digit
    n = n // 10
 
print(suma)
