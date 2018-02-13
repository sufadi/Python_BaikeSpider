# coding=utf-8
#!/usr/bin/python
# Python3 yield 生成器(generator)
'''
生成器是返回迭代器的函数，只能用于迭代操作

在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值
并在下一次执行next()方法时从当前位置继续运行
'''

'''
斐波那契
前面2个数相加等于第3个数值的特征
'''


def fibonacci(n):
    a = 0
    b = 1
    temp = a
    counter = 0

    while True:
        if(counter > n):
            return n

        print('遇到 next()就触发  返回 a = ', a)
        yield a
        '''
        a,b = b,a+b 等效于
        a=b
        b=a(原值)+b
        '''
        temp = a
        a = b
        b = temp + b
        counter = counter + 1
        print("大于2个 next()才触发  a = %d, b=%d" % (a, b))


# 返回迭代器,例如 0 1 1 2 3 5 8 13 21 34 55
f = fibonacci(10)

next(f)  # 0
next(f)  # 1
next(f)  # 1
next(f)  # 2
next(f)  # 3
