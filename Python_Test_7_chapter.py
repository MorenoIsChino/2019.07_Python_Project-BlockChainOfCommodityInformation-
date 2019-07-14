# 01.try-except 模式处理 error
print('####     01   ####')
# define the function to Calculate the sum
def sum(scores=[]):
    sumValue=0
    for item in scores:
        sumValue+=item
    return sumValue
# define the function to calculate the average scores
def mean_points(score=[],names=[]):
    try:
        all_score=sum(score)
        mean_score=all_score/len(names)
        print('学生的平均分是：%.2f'% mean_score)
        # if mean_score>100:
        #     raise UnNormalScoreInputError
    except ZeroDivisionError:
        print("Error：ZeroDivisionError\n出现了被 0 除的情况，很可能是没有添加学生名字列表")
    # except UnNormalScoreInputError:
    #     pass
    # UnNormalScoreInputError 是尝试定义的 Exception ，虽然在这里失败了 >_<
    # except BaseException as e:
    #     print("%s"%e)
    else:
        print("Successful operation")
#运行部分 1
print("运行部分 1")
score_1=[83,78,69,93,57]
names=['A','B','C','D','E']
mean_points(score_1,names)
#运行部分 2
print("运行部分 2")
score_2=[83,68,66,93,57]
# names=['A','B','C','D','E']
mean_points(score_2)


# 02.Bubble Sort & 变量数值互换
print('####     02   ####')
def bubbleSort_DescendingOrder(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] < list[j+1]:
                # python 中可以用 tuple 来进行特殊的变量数值互换
                list[j] ,list[j+1] = list[j+1],list[j]
                # print('in loop',list)
        # print('out loop', list)

list=[1,2,3,4,5]
print('Primitive list:\n',list)
bubbleSort_DescendingOrder(list)
print('Sorted list:\n',list)
