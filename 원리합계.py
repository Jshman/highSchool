# 단리법
# 원금 x (1 + 이율x기간)
print('원금 단위는 (만), 이율은 (%), 기간은 (개월)')
money, rate, term = map(float, input('원금, 이율, 기간 순으로 입력(구분은 공백을 하나 줌) : ').split(' '))
rate = rate/100
print('단리법', money * (1+rate*term))

# 복리법
# 원금 x (1+이율)
print('복리법', format(money * (1+rate)**term, ".2f"))
