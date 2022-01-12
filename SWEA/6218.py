a = int(input())

for b in range(1,a+1) :
    if a % b == 0 :
        print('%d(은)는 %d의 약수입니다.' % (b, a))
