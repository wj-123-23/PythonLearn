#
#
# def reg_stu(name, age, gender, city):
#     print(f"注册成功,姓名{name},年龄{age},性别{gender},city{city}")
#     return {'name': name, 'age': age, 'gender': gender, 'city': city}
#
# #位置传参
#
# stu1 = reg_stu("张三", 20, "男", "郑州")
# print(stu1)
# #关键字传参
# stu2 = reg_stu(name="李四", age=20, gender="男", city="上海")
# print(stu2)

#默认参数
# def reg_stu(name, age, gender, city='北京'):
#     print(f"注册成功,姓名{name},年龄{age},性别{gender},city{city}")
#     return {'name': name, 'age': age, 'gender': gender, 'city': city}
#
# stu = reg_stu(name="李四", age=20, gender="男")
# print(stu)


#不定长参数

#1 位置传参 (*args) args 随便起名 多个元素会封装到一个元组中
# def calc_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     return min_data, max_data, avg_data
#
# print(calc_data(4,44,88,99,55,12,45,65,85))
# print(calc_data(2,4,5,68,9,7,5,22))

#2 关键字传参(**kwargs) 封装为字典 字典的操作
def calc_data(*args,**kwargs):
    '''
    根据传入参数计算机最大值最小值平均值
    :param args: 不定长位置参数
    :param kwargs: 不定长关键字参数
        round:保留小数点个数
        print:是否打印输出
    :return:
    '''
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    if kwargs.get('round') is not None:
        avg_data = round(avg_data, kwargs.get('round'))
    if kwargs.get('print'):
        print(f'最小值{min_data}最大值{max_data}平均值{avg_data}')
    return min_data, max_data, avg_data

print(calc_data(4,44,88,99,55,12,45,65,85,round=3,print=True))
print(calc_data(2,4,5,68,9,7,5,22))