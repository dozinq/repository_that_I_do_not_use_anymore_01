a, b = input().split()
a = int(a)
b = int(b)

if b >= 45 :
    b -= 45
elif a >= 1 and b < 45 :
    a -= 1
    b += 15
else :
    a += 23
    b += 15

print ('%d %d' % (a, b))
