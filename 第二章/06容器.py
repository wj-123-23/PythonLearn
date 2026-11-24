#1.akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd
# a = 0
# b = 0
# ch = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
# for i in ch:
#     if i == 'a':
#         a +=1
#     elif i == 'k':
#         b +=1
# print(f"a的数量为{a},k的数量为{b}")

#6将如下多个列表合并为一个列表，并去重重复元素，排好序(升序)后输出到控制台。
# ist1 = ['M','A','C','E','F','6','H','L','N','I','3','K','0']
# list2 =['x','Z','T','Y','D','E','F','G']
# list3 = ['w', 'A', 'S', 'D']
# list4 = ist1 + list2 + list3
# new_list = []
# for item in list4:
#     if item not in new_list:
#         new_list.append(item)
# new_list.sort()
# print(new_list)

#7.将如下列表中能被3或5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,25, 26, 27, 28, 29, 30]
# new_list = []
# for item in list1:
#     if item % 2 == 0 and item % 5 == 0:
#         new_list.append(item)
# print(new_list)

# 8将如下列表中的正数提取出来，封装为一个新的列表
# list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
# new_list = []
# for item in list1:
#     if item > 0:
#         new_list.append(item)
# new_list.sort()
# print(new_list)

#9输入一个字符串，判断该字符串是否是回文(两边对称)
# s = input("输入一个字符串")
# print(s[::-1])
# if s == s[::-1]:
#     print("回文")
# over_str = str((str.split()).reverse())
# print(over_str)
# # for i in str:
# #     for j in str:
# #     if i in:
# #         print('该字符为回文')
# #     else:
# #         print(f"{i}不是回文")



# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下:
# 1.添加学生信息:根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2.修改学生信息:要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3.删除学生信息:要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4.查询学生信息:要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5.列出所有学生:遍历所有学生信息并输出。
# 6.统计班级成绩:统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学
# 员姓名。
# 7.退出系统
print("欢迎来到教务管理系统")
stu_sys = {}
# 菜单制作
menu = '''
######################
#    1.添加学生信息    # 
#    2.修改学生信息    # 
#    3.删除学生信息    # 
#    4.查询学生信息    # 
#    5.列出所有学生    # 
#    6.统计班级成绩    # 
#    7.退出系统       # 
######################
'''

while True:
    print(menu)
    choice = input("1-7请输入要进行的操作")
    # 1.添加学生信息:根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
    match choice:
        case "1":
            stu_name = input("请输入学生姓名")
            sco_chinese = float(input("请输入学生语文成绩"))
            sco_math = float(input("请输入学生数学成绩"))
            sco_english = float(input("请输入学生英语成绩"))

            if stu_name in stu_sys:
                print("该学生信息已存在")
            else:
                stu_sys[stu_name] = {"chinese": sco_chinese, "math": sco_math, "english": sco_english}
                print("学生添加完毕")
        # 2.修改学生信息:要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        case "2":
            stu_name = input("请输入学生姓名")
            if stu_name not in stu_sys:
                print("该同学的信息不存在")
                continue
            sco_chinese = float(input("请输入学生语文成绩"))
            sco_math = float(input("请输入学生数学成绩"))
            sco_english = float(input("请输入学生英语成绩"))
            stu_sys[stu_name] = {"chinese": sco_chinese, "math": sco_math, "english": sco_english}
            print("学生修改完毕")
        # 3.删除学生信息:要求输入要删除的学生姓名，根据姓名删除学生信息。
        case "3":
            stu_name = input("请输入学生姓名")
            if stu_name in stu_sys:
                del stu_sys[stu_name]
            else:
                print("该学生信息不存在")
        # 4.查询学生信息:要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        case "4":
            stu_name = input("请输入学生姓名")
            if stu_name in stu_sys:
                stu_info = stu_sys[stu_name]
                print(
                    f'该学生姓名为:{stu_name},语文成绩为:{stu_info['chinese']},数学成绩为:{stu_info['math']},英语成绩为:{stu_info['english']} ')
            else:
                print('该学生信息不存在')
        # 5.列出所有学生:遍历所有学生信息并输出。
        case "5":
            for stu_name in stu_sys:
                stu_info = stu_sys[stu_name]
                print(
                    f'学生姓名为:{stu_name},语文成绩为:{stu_info['chinese']},数学成绩为:{stu_info['math']},英语成绩为:{stu_info['english']} ')
        # 6.统计班级成绩:统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
        case "6":
            if not stu_sys:
                print("还没有学生信息")
                continue
                
            chinese_scores = []
            math_scores = []
            english_scores = []
            for stu_name,scores in stu_sys.items():
                chinese_scores.append(scores['chinese'])
                math_scores.append(scores['math'])
                english_scores.append(scores['english'])
            chinese_max = max(chinese_scores)
            math_max = max(math_scores)
            english_max = max(english_scores)

            chinese_min = min(chinese_scores)
            math_min = min(math_scores)
            english_min = min(english_scores)

            chinese_avg = sum(chinese_scores)/len(chinese_scores)
            math_avg = sum(math_scores)/len(math_scores)
            english_avg = sum(english_scores)/len(english_scores)

            for name,scores in stu_sys.items():
                if scores['chinese'] == chinese_max:
                    chinese_max_name = name
                if scores['math'] == math_max:
                    math_max_name = name
                if scores['english'] == english_max:
                    english_max_name = name
                if scores['chinese'] == chinese_min:
                    chinese_min_name = name
                if scores['math'] == math_min:
                    math_min_name = name
                if scores['english'] == english_min:
                    english_min_name = name
            print("===== 班级成绩统计 =====")
            print(f"语文 - 最高分: {chinese_max}, 最低分: {chinese_min}, 平均分: {chinese_avg:.2f}")
            print(f"     最高分学生: {chinese_max_name}")
            print(f"     最低分学生: {chinese_min_name}")

            print(f"数学 - 最高分: {math_max}, 最低分: {math_min}, 平均分: {math_avg:.2f}")
            print(f"     最高分学生: {math_max_name}")
            print(f"     最低分学生: {math_min_name}")

            print(f"英语 - 最高分: {english_max}, 最低分: {english_min}, 平均分: {english_avg:.2f}")
            print(f"     最高分学生: {english_max_name}")
            print(f"     最低分学生: {english_min_name}")
            print("========================")
        case "7":
            break
        case _:
            print("输入有误请重新输入")









# 7.退出系统