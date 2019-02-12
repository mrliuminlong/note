''''
python 绘制小猪
＠liu
2019-01-18
'''
from turtle import *
#绘制鼻子
def nose(x,y):
    penup()#提起笔
    goto(x,y)#定位
    pendown()#落笔，开始画
    setheading(-30)#将乌龟的方向设置为to-angle/为数字（0－东，90－北，180－西，270－南）
    begin_fill()#准备填充图形
    a = 0.4
    for i in range(120):
        if 0 <= i <30 or 60<=i<90:
            a = a + 0.08
            left(3)#向左转3度
            forward(a)#向前走步长a
    end_fill()#填充完成

    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    pencolor(255,155,192)#画笔颜色
    setheading(10)
    begin_fill()
    circle(5)
    color(160,82,45)
    end_fill()
def head(x,y):#画头
    color((255,155,192),'pink')
    penup()
    goto(x,y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300,-30)
    circle(100,-60)
    circle(80,-100)
    circle(150,-20)
    circle(60,-95)
    setheading(161)
    circle(-300,15)
    penup()
    goto(-100,100)
    pendown()
    setheading(-30)
    a = 0.4
    for i in range(60):
        if 0<=i<30 or 60<=i<90:
            a += 0.08
            left(3)
            forward(a)
        else:
            a -= a-0.08
            left(3)
            forward(a)
    end_fill()

def check(x,y):#腮
    color((255,155,192))
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()

def mouth(x,y):#嘴巴
    color(239,69,19)
    penup()
    goto(x,y)
    pendown()
    setheading(-80)
    circle(30,40)
    circle(40,80)

def eyes(x,y):#眼睛耳朵
    color(239,69,19)
    penup()
    goto(x,y)
    pendown()
    setheading(-80)
    circle(30,40)
    circle(40,80)

# def ears(x,y):#耳朵
#     color(239,69,19)
#     penup()
#     goto(x,y)
#     pendown()
#     setheading(-80)
#     circle(30,40)
#     circle(40,80)

def setting():#参数设置
    pensize(4)
    # hideturtle()#使得乌龟隐藏
    colormode(255)#将其设置1.0或者255，颜色的三元组必须在这个范围内
    color((255,155,192),'pink')
    setup(840,500)
    speed(1)

def main():
    setting()#画布画笔设置
    nose(-100,100)#鼻子设置
    head(-69,167)#头设置
    # ears(0,160)#耳朵
    # eyes(0,140)#眼睛
    check(80,10)#腮
    mouth(-20,30)#嘴
    done()

if __name__=='main':
    main()

main()