import sys, math
a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])

x = (-b + math.sqrt((b)**2-4*a*c))/(2*a)
y = (-b - math.sqrt((b)**2-4*a*c))/(2*a)
print(int(x))
print(int(y)) 