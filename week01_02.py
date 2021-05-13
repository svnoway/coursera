import sys


levels_count = int(sys.argv[1])
for i in range(levels_count,0,-1):
    print(' '*(i-1)+'#'*(levels_count-i+1))