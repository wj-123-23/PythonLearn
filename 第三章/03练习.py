# #.定义一个函数:根据传入的底和高计算三角形面积的函数(三角形面积=底*高/2)。
# from idlelib.tree import listicons
#
#
# def triangle_area(b,h):
#     '''
#     根据传入底和高计算三角形的面积
#     :param b: 底
#     :param h: 高
#     :return: 三角形面积
#     '''
#     area = b * h / 2
#     return round(area, 2)
# area = triangle_area(3,4)
# print(area)
#
#
# #2.定义一个函数:计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIOU)。
# def count_aeiou(w):
#     num = 0
#     for i in w:
#         if i in 'aeiouAEIOU':
#             num += 1
#     return num
# print(count_aeiou('aeiouAEIOUaaaaaa'))



# #3.定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。
# def statistics(score_list):
#     '''
#     根据传入一个list s_list = [] 统计最高分,最低分,及平均分
#     :param score_list: 分数列表
#     :return: 最高分,最低分,及平均分
#     '''
#     max_score = max(score_list)
#     min_score = min(score_list)
#     avg_score = round(sum(score_list) / len(score_list),1)
#     return max_score, min_score, avg_score
# s_list = [500,689,504,205,404,405,687,568]
# max_score, min_score, avg_score = statistics(s_list)
# print("最高分:",max_score)
# print("最低分:",min_score)
# print("平均分:",avg_score)
# #4.定义一个函数，根据传入的分数，计算对应的分数等级并返回。分数>= 90:A分数>=75:B分数>=60:C分数<60:D
# def count_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 75:
#         return "B"
#     elif score >= 60:
#         return "C"
#     elif score < 60:
#         return "D"
#
# grade = count_grade(99)
# print(grade)
#



# #5.定义一个函数，用于判断一个字符串是否是回文串，返回bool值。把字符串反转，如果和原字符串相同，就是回文串。(如:"level"，"radar"，"黄山落叶松叶落山黄")
# def palindrome(st):
#         if st == st[::-1]:
#             return True
#         else:
#             return False
# st = "radsar"
# print(palindrome(st))
#
#
# def palindrome(st):
#     left = 0
#     right = len(st) - 1
#     while left < right:
#         if st[left] != st[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
#
#
# print(palindrome("radar"))                # True
# print(palindrome("level"))                # True
# print(palindrome("radsar"))               # False
# print(palindrome("黄山落叶松叶落山黄"))     # True
# print(palindrome("a"))                    # True
# print(palindrome(""))                     # True

#6.定义一个函数:完成时间转换功能，将传入的秒转换为小时、分钟、秒。
def time_count(second):
    if second <60:
        return 0,0,second
    if second <3600:
        minutes = second // 60
        rest_second = second % 60
        return 0,minutes , rest_second
    else:
        hours = second // 3600
        rest = second % 3600
        rest_minute = rest // 60
        rest_second = rest % 60
        return hours,rest_minute,rest_second
hour,minute,second=time_count(3661)
print(hour,minute,second)   # 1小时1分钟1秒
print(time_count(59))       # 0小时0分钟59秒


def time_count(second):
    hours = second // 3600
    minutes = (second % 3600) // 60
    seconds = second % 60
    return f"{hours}小时{minutes}分钟{seconds}秒"


print(time_count(3661))   # 1小时1分钟1秒
print(time_count(59))     # 0小时0分钟59秒
#7.定义一个函数:根据传入的三角形三个边的边长，判定三角形的类型(等边、等腰、普通，或者不能构成三角形)。
