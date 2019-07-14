import json
from basicFunction.hashCodeGeneration import hashCodeGenerate
from judgment.blockChainStatus import returnBlockChainStatus

# 输入：商品名
# 结果：.json 文件的最后一个区块的哈希值
# tips:只适用于刚加入信息的区块
def updateLastBlockValue(commodityName):
    # 从对应文件夹中读取区块链数据
    fileJson=commodityName+'.json'
    with open(fileJson,'r',encoding='utf-8') as fOpen:
        dataOfBlockChain=json.load(fOpen)

    statusOfBlockChain=returnBlockChainStatus(commodityName)
    lastIndex=str(statusOfBlockChain)
    lastSecondIndex=str(statusOfBlockChain-1)

    # 需要更新计算哈希值的种情况：
    # 1.只有一个区块链但 current_hash 为‘该区块哈希值’
    # 2.有多个区块，但最后一个区块的 pre_hash 不等于前一个区块的 current_hash
    if (statusOfBlockChain==1 and dataOfBlockChain['1']['current_hash']=='该区块哈希值'):
        print('status:',statusOfBlockChain)
        # 将用作计算的信息作为一个字符串
        # dataForHash=商品名+时间+位置+用户+电话+详细描述
        dataForHash=commodityName+dataOfBlockChain['1']['infor']['event_time']
        dataForHash=dataForHash+dataOfBlockChain['1']['infor']['location']
        dataForHash=dataForHash+dataOfBlockChain['1']['infor']['person']
        dataForHash=dataForHash+dataOfBlockChain['1']['infor']['tel']
        dataForHash=dataForHash+dataOfBlockChain['1']['infor']['describe']
        output=hashCodeGenerate(dataForHash)
        # output 为返回的二元组，第一个是哈希值，第二个是随机数
        dataOfBlockChain['1']['current_hash']=output[0]
        dataOfBlockChain['1']['random_num']=output[1]


    elif (statusOfBlockChain>=2 and statusOfBlockChain<=5 and dataOfBlockChain[lastIndex]['pre_hash']!=dataOfBlockChain[lastIndex]['current_hash']):
        print('status:', statusOfBlockChain)
        # 赋值前哈希值
        dataOfBlockChain[lastIndex]['pre_hash']=dataOfBlockChain[lastSecondIndex]['current_hash']
        # 将用作计算的信息作为一个字符串
        # dataForHash=商品名+时间+位置+用户+电话+详细描述
        dataForHash = commodityName + dataOfBlockChain[lastIndex]['infor']['event_time']
        dataForHash = dataForHash + dataOfBlockChain[lastIndex]['infor']['location']
        dataForHash = dataForHash + dataOfBlockChain[lastIndex]['infor']['person']
        dataForHash = dataForHash + dataOfBlockChain[lastIndex]['infor']['tel']
        dataForHash = dataForHash + dataOfBlockChain[lastIndex]['infor']['describe']
        output = hashCodeGenerate(dataForHash)
        # output 为返回的二元组，第一个是哈希值，第二个是随机数
        dataOfBlockChain[lastIndex]['current_hash'] = output[0]
        dataOfBlockChain[lastIndex]['random_num'] = output[1]

    # 将修改后的数据存储在对应的 .json 文件
    with open(fileJson,'w',encoding='utf-8') as fClose:
        json.dump(dataOfBlockChain,fClose)