#求100内的奇数
# L = []
# for x in range(101):
#     if x%2 == 1:
#         # print(x)
#         L.append(x)
# print(L)


# L = [x for x in range(101) if x%2 == 1]
# print(L)


# def myodd(n):
#     return n%2==1
# fill = filter(myodd, range(101))
# for item in fill:
#     print(item)


# print([item for item in filter(lambda x:x%2==1, range(101))])

#偏函数
from functools import partial
num = int(input("enter a integer!"))
def myodd(m,n):
    return m%n
y_100 = partial(myodd, 100)
print('100对%d求余数:'%num, y_100(num))
