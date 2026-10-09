# -*- coding: utf-8 -*-
"""
Day 01 自动判分器
- 读取 01_variables.py，执行它，逐个检查变量名和值。
- 做一题判一题，没做的直接扣分。
- 这个文件是判分标准，改它不算本事。
"""
import os
import sys
import traceback

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(HERE, '01_variables.py')

if not os.path.exists(TARGET):
    print('[致命] 找不到 01_variables.py，你是不是把它删了？')
    sys.exit(1)


# ---------- 执行学生的作业文件 ----------
src = open(TARGET, encoding='utf-8-sig').read()   # 兼容带/不带 BOM
ns = {
    '__name__': '__main__',
    '__file__': TARGET,
    'input': lambda *a, **k: '',          # 屏蔽 input，防止卡住
}
run_error = None
err_line = None
try:
    exec(compile(src, TARGET, 'exec'), ns)
except Exception as e:
    run_error = e
    for fr in reversed(traceback.extract_tb(e.__traceback__)):
        if os.path.abspath(fr.filename) == os.path.abspath(TARGET):
            err_line = fr.lineno
            break


def get(name):
    """取变量；没定义就返回哨兵，避免和 None 混淆。"""
    return ns[name] if name in ns else _MISSING


class _Missing:
    def __repr__(self):
        return '<未定义>'


_MISSING = _Missing()


def is_int(v):
    return isinstance(v, int) and not isinstance(v, bool)


# ---------- 判分规则 ----------
results = []


def check(no, title, fn, hint):
    try:
        ok, detail = fn()
    except Exception as e:
        ok, detail = False, '判分时出错: %r' % e
    results.append((no, title, ok, detail, hint))


# 1
def c1():
    v = get('my_age')
    if v is _MISSING:
        return False, '变量 my_age 不存在'
    if not is_int(v):
        return False, 'my_age 的类型是 %s，要求 int' % type(v).__name__
    if not (10 <= v <= 99):
        return False, 'my_age = %r，这个年龄不离谱吗' % (v,)
    return True, 'my_age = %r' % (v,)


check(1, '定义整数变量 my_age', c1, 'my_age = 20')


# 2
def c2():
    v = get('my_name')
    if v is _MISSING:
        return False, '变量 my_name 不存在'
    if not isinstance(v, str):
        return False, 'my_name 的类型是 %s，要求 str' % type(v).__name__
    if v.strip() == '':
        return False, 'my_name 是空字符串'
    return True, 'my_name = %r' % (v,)


check(2, '定义字符串变量 my_name', c2, 'my_name = "王健"')


# 3
def c3():
    v = get('pi_approx')
    if v is _MISSING:
        return False, '变量 pi_approx 不存在'
    if not isinstance(v, float):
        return False, 'pi_approx 的类型是 %s，要求 float（3.14 比 3 多了小数点才是 float）' % type(v).__name__
    if abs(v - 3.14) > 1e-9:
        return False, 'pi_approx = %r，要求 3.14' % (v,)
    return True, 'pi_approx = %r' % (v,)


check(3, '定义浮点变量 pi_approx', c3, 'pi_approx = 3.14')


# 4
def c4():
    v = get('is_student')
    if v is _MISSING:
        return False, '变量 is_student 不存在'
    if not isinstance(v, bool):
        return False, 'is_student 的类型是 %s，要求 bool（True 不要加引号）' % type(v).__name__
    if v is not True:
        return False, 'is_student = %r，要求 True' % (v,)
    return True, 'is_student = True'


check(4, '定义布尔变量 is_student', c4, 'is_student = True')


# 5
def c5():
    g = get('greeting')
    name, age = get('my_name'), get('my_age')
    if g is _MISSING:
        return False, '变量 greeting 不存在'
    if name is _MISSING or age is _MISSING:
        return False, '先把第 1、2 题做完才能判这题'
    if not isinstance(g, str):
        return False, 'greeting 的类型是 %s，要求 str' % type(g).__name__
    expect = '我是%s，今年%s岁' % (name, age)
    if g != expect:
        return False, 'greeting = %r，要求的格式是 %r' % (g, expect)
    return True, 'greeting = %r' % (g,)


check(5, 'f-string 拼装 greeting', c5, 'greeting = f"我是{my_name}，今年{my_age}岁"')


# 6
def c6():
    v, name = get('name_upper'), get('my_name')
    if v is _MISSING:
        return False, '变量 name_upper 不存在'
    if name is _MISSING or not isinstance(name, str):
        return False, '先把第 2 题做完才能判这题'
    if not isinstance(v, str):
        return False, 'name_upper 的类型是 %s，要求 str' % type(v).__name__
    if v != name.upper():
        return False, 'name_upper = %r，期望 %r' % (v, name.upper())
    return True, 'name_upper = %r' % (v,)


check(6, '字符串大写 name_upper', c6, 'name_upper = my_name.upper()')


# 7
def c7():
    v, name = get('name_len'), get('my_name')
    if v is _MISSING:
        return False, '变量 name_len 不存在'
    if name is _MISSING or not isinstance(name, str):
        return False, '先把第 2 题做完才能判这题'
    if not is_int(v):
        return False, 'name_len 的类型是 %s，要求 int' % type(v).__name__
    if v != len(name):
        return False, 'name_len = %r，但 len(my_name) = %d' % (v, len(name))
    return True, 'name_len = %r' % (v,)


check(7, '字符串长度 name_len', c7, 'name_len = len(my_name)')


# 8
def c8():
    v = get('total')
    if v is _MISSING:
        return False, '变量 total 不存在'
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        return False, 'total 的类型是 %s，要求数字' % type(v).__name__
    expect = round(19.9 * 3, 2)
    if abs(v - expect) > 1e-9:
        return False, 'total = %r，期望 %r' % (v, expect)
    return True, 'total = %r' % (v,)


check(8, '乘法 + round 保留两位', c8, 'total = round(price * count, 2)')


# 9
def c9():
    v = get('num_int')
    if v is _MISSING:
        return False, '变量 num_int 不存在'
    if not is_int(v):
        return False, 'num_int 的类型是 %s，要求 int' % type(v).__name__
    if v != 42:
        return False, 'num_int = %r，期望 42' % (v,)
    return True, 'num_int = %r' % (v,)


check(9, '字符串转整数 num_int', c9, 'num_int = int(num_str)')


# 10
def c10():
    v = get('type_ok')
    if v is _MISSING:
        return False, '变量 type_ok 不存在'
    if not isinstance(v, bool):
        return False, 'type_ok 的类型是 %s，要求 bool' % type(v).__name__
    if v is not True:
        return False, 'type_ok = %r，期望 True' % (v,)
    return True, 'type_ok = True'


check(10, '用 type() 做判断 type_ok', c10, 'type_ok = (type(42) == int)')


# ---------- 输出 ----------
W = 62
print('=' * W)
print('  Day 01 · 变量与数据类型 · 判分结果')
print('=' * W)

if run_error is not None:
    loc = '第 %d 行' % err_line if err_line else '未知行'
    print()
    print('  [!] 你的代码在 %s 运行时报错了：' % loc)
    print('      %s: %s' % (type(run_error).__name__, run_error))
    print('      —— 报错之前的题照样判，后面没跑到的题按 0 分算。')
    print()

passed = 0
for no, title, ok, detail, hint in results:
    mark = '  OK  ' if ok else ' FAIL '
    print('[%s] %2d. %s' % (mark, no, title))
    print('         %s' % detail)
    if not ok:
        print('         参考写法: %s' % hint)
    if ok:
        passed += 1

score = passed * 10
print('-' * W)
print('  得分: %d / 100    （对 %d 题，错/漏 %d 题）'
      % (score, passed, len(results) - passed))
print('-' * W)
print()

if score == 100:
    print('  满分。但别高兴太早——这十题是「打字」，不是「编程」。')
    print('  真正的门槛在后面：函数、循环、把数据和逻辑分开。')
elif score >= 70:
    print('  及格。错的那些题，回去把代码重敲一遍，别只改那一行。')
elif score >= 30:
    print('  一半都不到。这说明你看教程的时候，脑子是「跟上了」的，手是没跟上的。')
    print('  把没过的题重写，再跑一次。')
else:
    print('  这个分数说明：你刚才那半小时，还是在「看」，不是「写」。')
    print('  别往下学了。把这 10 题写到 100 分，再开下一课。')
print()
