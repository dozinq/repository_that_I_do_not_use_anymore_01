a = [88, 30, 61, 55, 95]
num = 1

for i in a:
    if i >= 60:
        print('%d번 학생은 %d점으로 합격입니다.' % (num, i))
    else:
        print('%d번 학생은 %d점으로 불합격입니다.' % (num, i))
    num += 1
