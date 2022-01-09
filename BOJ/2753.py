year = int(input())
result = 0

if year % 4 == 0 :
    result = 1
if year % 100 == 0 :
    result = 0
if year % 400 == 0 :
    result = 1

print('%d' % result)
