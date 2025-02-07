# 코흐의 눈송이 그리기
from turtle import *

def koch(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(a / 3, order - 1)
            left(t)
    else:
        forward(a)

# 색깔, 크기, 횟수
color("sky blue", "white")
bgcolor("black")
size = 400
order = 8


# 그림 가운데로 정렬
penup()
backward(size/1.732)
left(30)

pendown()

# 빠르게 그리도록하는 함수
tracer(1000) #속도
hideturtle()

begin_fill()

# 똑같이 3번 그려서 눈송이로 만듦.
for i in range(3):
    koch(size, order)
    right(120)

end_fill()

# 보이기
update()

import math

#어느 도형의 길이를 x배 크게 만들었을 때 그 도형의 면적이나 부피가 n배 증가한다고 가정하면, 그 도형의 차원은 다음과 같습니다.
Round1 = 1 * (4/3)**order
Round2 = 2 * (4/3)**order
Round3 = 3 * (4/3)**order

print("한 변의 길이가 1일 때 둘레는 : ", Round1)
print("한 변의 길이가 2일 때 둘레는 : ", Round2)
print("한 변의 길이가 3일 때 둘레는 : ", Round3)

#삼각형의 넓이
#print("길이 1 넓이: ", (3**0.5)/4 * order)
#print("길이 2 넓이: ", (3**0.5)/4 * 2 * order)
#print("길이 3 넓이: ", (3**0.5)/4 * 3 * order)

# 코흐의 삼각형의 차원
x = 4 # (n+1) 단계가 되었을 때의 선분 개수
base = 1/3 # n 단계에서 (n+1)단계로 갈 때의 길이 비
Dimention = "{0:.2f}".format(math.log(x,1/base))

print("코흐의 삼각형의 차원은? 약", Dimention)
