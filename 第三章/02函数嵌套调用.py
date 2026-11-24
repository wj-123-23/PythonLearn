def function_a():#嵌套函数,遵循栈的逻辑(先进后出)
     print('A')
     function_b()
     print('B')

def function_b():
    print('c')
    function_c()
    print('d')

def function_c():
    print('e')

function_a()