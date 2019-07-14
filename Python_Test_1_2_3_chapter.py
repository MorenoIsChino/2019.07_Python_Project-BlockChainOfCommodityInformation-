#1.测试关键字 'in'&'not in'
print('####     01    ####')
print('h'in 'hello World')

#2.测试关键字'is’和'is not'
print('####     02    ####')
x=1
y=x+1
print(x is y)
print(id(x))
print(id(y))
print(x is not y)

#3.字符串拼接
print('####     03    ####')
print('Hello\t'+'Python')
print(('I\'m fine.'+'\n')*4)

#4.用占位符进行格式化输出
print('####     04    ####')
x=1
y=1.1
xy='第一个是int类型 %d\n第二个是浮点数类型 %.2f'%(x,y)
print(xy)

#5.用 format()函数 进行格式化输出
print('####     05    ####')
# 不设置指定位置，按默认顺序
x1="{} {}".format("hello", "world")
print(x1)#print() ，默认情况下是输出一行
#
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

#6.用 index 截取 string
print('####     06    ####')
stringWithIndex="0123456789"
str1=stringWithIndex[0:4]#括号里的整数相当于数组的下标，包前不包后
print(str1)

#2.2.3技能实训
print('####     2.2.3技能实训    ####')
strHappy="  haPPy BiRthDay To u "
strHappy=strHappy.strip()
strHappy=strHappy.lower()
strHappy=strHappy.replace('u','you')
print(strHappy)

#3.1.4技能实训
print('####     3.1.4技能实训    ####')
"""

originalPrice=5000.00
month=input('乘飞机的月份是：')#input函数里可以输出一些字符串
month=int(month)
print('mouth is : %d'%month)
siteKind=input('乘飞机的座位等级是 头等舱 OR 经济舱 ?:')
print('siteKind is : %s'%siteKind)
#逻辑结构
if month>=4 and month<=10:
    if siteKind=="头等舱":
        originalPrice=originalPrice*0.9
    else:
        originalPrice=originalPrice*0.6
else:
    if siteKind=="头等舱":
        originalPrice=originalPrice*0.5
    else:
        originalPrice=originalPrice*0.4
#print the final price
print("actual price is : %0.2f"%originalPrice)
"""

#7.测试 for 循环与 range() 函数
print('####     07    ####')
#bit=0
for bit in range(0,101,20):
    print(bit)
print('another way')
for bit in range(5):
    print(bit)
#注意循环结构中条件后的 ：
#range() 函数的三个参数中，前两个表示数列范围，左闭右开，如题为[0,101);第三个参数可无，表示递进的步长（或等差）

#3.2.3
# 技能实训
print('####     3.2.3技能实训    ####')
end=1
minValue=0
maxValue=0
intType=1
#逻辑结构
while end!=0:
    print("请输入一个整数（输入0作为结束）：",end="")
    end=input()
    end=int(end)
    if type(end)!=type(intType):
        print("\nThe type is not int,please input again")#忽略这里没卵用的纠错机制
        continue
    else:
        if minValue>=end:
            minValue=end
        elif maxValue<=end:
            maxValue=end
        else:
            continue
#输出信息
print("最大值： %d  最小值： %d"%(maxValue,minValue))#有多个格式化参数时变量用括号封装起来