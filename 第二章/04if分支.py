#1
# num = int(input("请输入一个数字"))
# if num%2 == 0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")
#2
# age = int(input("请输入年龄"))
# if age >= 18:
#     print("成年")
# else:
#     print("未成年")
#3
# num = int(input("请输入一个数字"))
# if num > 0:
#     print(f"{num}是正数")
# else:
#     print(f"{num}是负数")
#4
# score = float(input("输入成绩"))
# if score >= 60:
#     print("及格了")
# else:
#     print("不及格")
#5
# score = float(input("输入成绩"))
# if score >= 85:
#     print("优秀")
# elif score >=60 and score <= 85:
#     print("及格")
# else:
#     print("不及格")
from html.parser import charref

#6
# sum = float(input("总金额"))
# if sum >= 500:
#     fact_money = sum * 0.8
#     print(f"实际金额为{fact_money}")
# elif sum >= 300 and sum < 500:
#     fact_money = sum * 0.9
#     print(f"实际金额为{fact_money}")
# elif sum >= 100 and sum < 300:
#     fact_money = sum * 0.95
#     print(f"实际金额为{fact_money}")
# else:
#     fact_money = sum
#     print(f"实际金额为{fact_money}")

#7
# land1 = int(input("输入一个边长"))
# land2 = int(input("输入一个边长"))
# land3 = int(input("输入一个边长"))
# if land1 + land2 > land3 or land1 + land3 > land2 or land2 + land3 > land1:
#     if land1 == land2 == land3:
#         print("该三角形为等边三角形")
#     elif land1 == land2 or land3 == land1 or land3 == land2:
#         print("该三角形为等腰三角形")
#     else:
#         print("该三角形为普通三角形")
# else:
#     print("不能构成三角形")
#8
# day = input('请输入1-7')
# match day:
#     case '1':
#         print("周一")
#     case '2':
#         print("二")
#     case '3':
#         print("周三")
#     case '4':
#         print("周四")
#     case '5':
#         print("周五")
#     case '6':
#         print("周六")
#     case '7':
#         print("周日")
#     case _:
#         print("有无")

#9
num1 = float(input("请输入一个数"))
num2 = float(input("请输入一个数"))
char = input("输入符号+-*/")

match char:
    case "+":
        print(f"{num1}+{num2}={num1+num2}")
    case "-":
        print(f"{num1-num2}")
    case "*":
        print(f"{num1*num2}")
    case "/":
        print(f"{num1/num2}")