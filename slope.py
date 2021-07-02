import math
a = int(input())
b = int(input())
slope_m = a/(-1*b)
slope_b = b/a
print(round(math.atan(slope_b)))
