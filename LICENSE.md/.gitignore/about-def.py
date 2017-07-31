#!/usr/bin python2.7
# -*- coding:utf-8 -*-
#  1观察作用域
'''a = "this is a golbal variable"

def foo():
    print locals()

print globals()
foo()
'''
# 2命名空间
'''a = "this is a golbal variable"
def foo():
    #a = "text"     #函数内的变量是局部变量是单独定义的新变量和全局变量不是同一个
    print locals()
    print a
    

foo()
print a
'''
# 3变量生存周期
'''def foo():
    x = 1
    def foo2():
        print x

    return None
foo()
'''
# 4函数参数
'''def foo(x):
    print locals()

foo(1)

def foo(a,b,**c):
    print a,b
    print c
    for x in c:
        print x,':',str(c[x])


foo(1,2,d = 'hello',c = 200)
'''
# 5嵌套函数
'''y = 2
def outer(x):
    x = 1
    def inner():
        print x
        print y
    inner()  #类似于普通调用全局变量,但是所有函数都在全局中

outer(3)
'''
# 6函数是一级类对象
'''print issubclass(int,object)

def foo():
    pass
print foo.__class__

print issubclass(foo.__class__,object)

def add(x,y):
    return x+y
def sub(x,y):
    return x-y

def apply(a,x,y):
    return a(x,y)

print apply(add,10,1)

print apply(sub,10,9)
'''
# 7闭包
'''def outer():
    x = 1
    def inner():
        print x
    return inner

foo = outer()
foo()

def outer(x):

    def inner(y):
        print '1',y**x
        return '2',y**x
    return inner

foo = outer(4)

print '3',foo(2)
'''
#  8装饰器

'''def outer(some_func):
    def inner():
        print "befor some_func"
        ret = some_func()
        return ret + 1
    return inner

def foo():
    return 1


decorated = outer(foo)
print decorated()
print '//////////////////////'

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Coord: " + str(self.__dict__)

# 一般方法
def add(a,b):
    return Coordinate(a.x + b.x, a.y + b.y)

def sub(a,b):
    return Coordinate(a.x - b.x, a.y- b.y)


one = Coordinate(100 , 200)
two = Coordinate(300 , 200)
three = Coordinate(-100, -100)
print add (one, two)
c = Coordinate(1,2)

# 装饰器
def wrapper(func):
    def checker(a, b):
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > o else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret
    return checker

add = wrapper(add)
sub = wrapper(sub)
print sub (one, two),add (one,three)

# 9 @标识符将装饰器应用到函数
@wrapper
def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)
'''

#  10 *arg & **kwargs
'''def one(*args):
    print args

one()
one(1,2,3)

def two(x, y, *args):
    print x, y, args

two('a','b','c')

def add(x, y):
    return x + y

lst = [1,2]
print add(lst[0], lst[1])
print add(*lst)

def foo(**kwargs):
    print kwargs

foo()
foo(x = 1, y = 2)

dct = {'x': 1, 'y' : 2}

def bar(x, y):
    print x + y

bar(**dct)  #使用时字典噶和参数数必须一致
'''
# 11完全版的装饰器
'''
def logger(func):
    def inner(*args, **kwargs):
        print 'Arguments were: %s, %s' %(args, kwargs)
        return func(*args, **kwargs)

    return inner

@logger
def foo1(x, y = 1):
    return x * y

@logger
def foo2():
    return 2

print foo1(5, 4)

print foo1(1)

foo()
'''
