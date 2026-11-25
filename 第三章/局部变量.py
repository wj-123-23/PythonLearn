num = 100
w= 20
def cirle_area(r):
    pi = 3.14 #pi & area为局部变量 只能在函数内部访问
    #num & w 为全局变量 在函数内部改变 不会改变函数外部
    area = pi * r * r
    num = 1000
    global w
    w = 30
    print(num)
    return area


c_area = cirle_area(10)
print(c_area)
print(num)
print(w)

