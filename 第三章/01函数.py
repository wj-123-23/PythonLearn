import math


def circle_area(r):#'''''' 函数说明文档,帮助维护函数 help() 鼠标放在函数上查看
    '''
    根据圆的半径求圆的面积
    :param r:圆的半径
    :return:圆的面积
    '''
    area = 3.14 * r * r
    return round(area, 2)#数,保留几位小数
help(circle_area)
area = circle_area(3)
print(area)

def rectangle_area(l, w):
    area = l * w
    return area

print(rectangle_area(4, 5))

def circle_area_len(r):
    return 3.14 * r * r , 3.14 * r * 2 #多个返回值 逗号分割,返回为元组
print(circle_area_len(4))
print(type(circle_area_len(4)))

area , len = circle_area_len(4)
print(area, len)#解包


