#1.Data Structure:list,and two kinds of list's index
print('####     01    ####')
salary=[0,1,2,3,4,'aa',6]#list 可以存放不同类型的数据
print(salary)
print(salary[0])#正向索引
print(salary[-1])#反向索引
print(salary.__len__())#返回list的长度

#2.some function of list
print('####     02    ####')
#append
print('_append_')
list=[0,1,2,3,4,5,6,7,8,9]
list.append(10)
print(list)
#insert
print('_insert_')
list=[0,1,2,3,4,5,6,7,8,9]
list.insert(1,10)
print(list)
#pop
print('_pop_')
list=[0,1,2,3,4,5,6,7,8,9]
list.pop()#if don't have index,remove the final object in default
print(list)
#元素赋值
print('_元素赋值_')
list=[0,1,2,3,4,5,6,7,8,9]
list[9]=100
print(list)
#delete one element
print('_delete one element_')
list=[0,1,2,3,4,5,6,7,8,9]
del list[9]
print(list)

#3.Data Structure:tuple-Unmodifiable List
print('####     03    ####')
tuple_1=(0,1,2,3,4)
print(tuple_1)
#tuple_1[0]=2
#print(tuple_1)

#3. 4.2.3技能实训
print('####     4.2.3技能实训    ####')
#将《诗经 桃夭》储存在字符串之中
originalText="桃之夭夭，灼灼其华。之子于归，宜其室家。桃之夭夭，有蕡其实。之子于归，宜其家室。桃之夭夭，其叶蓁蓁。之子于归，宜其家人。"
#统计字符串长度，用于检索每一个字的索引
lengthOfOriginalText=originalText.__len__()
#用无关信息创建一个新的 字典 dict
dictOfText={"Start":'useless information'}
#遍历字符串，如果一个字符存在，给value++；如果不存在，追加这个字符，并且value=1
loopTimes=1
listOfIndex=[]#创建一个list,用于储存dict中的index
while loopTimes<=lengthOfOriginalText:
    if originalText[loopTimes-1] in dictOfText:
        dictOfText[originalText[loopTimes-1]]=dictOfText[originalText[loopTimes-1]]+1#对应的次数自增
    else:
        dictOfText[originalText[loopTimes - 1]] =1
        listOfIndex.append(originalText[loopTimes - 1])#在第一次见到某个字符时，将它记录在list中
    loopTimes=loopTimes+1
# for循环 打印每个字符以及出现的次数
print("_character_            _times_")
for character in listOfIndex:
    print(character,"                    ",end="")
    print(dictOfText[character])
#这里使用list的原因在于，list中的元素有序，输出时可以按照他们在文中出现的顺序


