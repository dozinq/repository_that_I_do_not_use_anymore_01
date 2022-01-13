a = int(input())
n = 0

for i in range(1, a+1) :
    if a % i == 0 :
        print("%d(은)는 %d의 약수입니다." %(i, a))
        n += 1

if n == 2 :
    print(("%d(은)는 %d과 %d로만 나눌 수 있는 소수입니다." % (i, 1, i)))
