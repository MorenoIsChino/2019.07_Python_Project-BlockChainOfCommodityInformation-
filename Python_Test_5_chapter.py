# 1.function: Indefinite length parameter
print('####     01    ####')
def indefiniteLenParameterFunc(*index):#1.注意定义函数的引号 2.不定长参数，会被作为一个元组传入
    data=[0,1,2,3,4,5,6,7,8,9,10]
    for item in index:
        print(data[item],"\t")
indefiniteLenParameterFunc(2,5,6,9)

# 2.包裹关键字参数的 function
print('####     02    ####')
def keywards_avg(**kwargs):  #传入的kwargs是一个dict
    for key in kwargs:
        print(key+"avg is:")
        data=kwargs[key] #利用 key 得到对应的 value
        sum=0
        for item in data:
            sum+=item
        avg=sum/len(data)
        print(avg,"\t")
keywards_avg(first_key_value=[1,2,3,4],second_key_value=[5,6,7,8])
#    为了不出冲突，多种参数排列的原则为 def func(位置参数，包裹位置参数，默认参数，包裹关键字参数)

# 3.关键字 yield
print('####     03   ####')
def generate_sequence():
    for i in range(3):
        print('return ',i)
        yield i
print("call generate_sequence():")
generate_sequence=generate_sequence()
print("print\t ",generate_sequence.__next__())
print("print\t ",generate_sequence.__next__())
print("print\t ",generate_sequence.__next__())
# __next__() is a function for all of iterator,it will return the next value of iterator


# 4.use random module
print('####     04   ####')
# 导入随机数模块
import random
# get an random number in [0,99]
for count in range(20):
    random_int=random.randint(0,99)
    print(random_int," ",end="") # end="" 意味着不换行
print() # new line

# 5.use random module ：2nd way
print('####     05   ####')
# 导入随机数模块
from random import randint
# get an random number in [0,99]
for count in range(20):
    random_int=randint(0,99)
    print(random_int," ",end="") # end="" 意味着不换行
print()

# 6.use random module ：3nd way
print('####     06   ####')
# 导入随机数模块
from random import randint as suiJiShu #给导入的包加了别名后，可以用别名调用模块中的 calss or function ，但不能再用原名
# get an random number in [0,99]
for count in range(20):
    random_int=suiJiShu(0,99)
    print(random_int," ",end="") # end="" 意味着不换行
print()

# 7. calculate the variance
print('####     07   ####')
import pandas as pd
# 计算方差 pandas  是 Anaconda 中用于计算方差的 package
turn_over_a=pd.Series([1,1,1,1,1,1,1,1,1,1,1,1])
print(turn_over_a.var())
