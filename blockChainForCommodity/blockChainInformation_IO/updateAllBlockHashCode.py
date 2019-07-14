import json
from basicFunction.hashCodeGeneration import hashCodeGenerate
from judgment.blockChainStatus import returnBlockChainStatus

def updateAllHashCode(commodityName):
    # 从对应文件夹中读取区块链数据
    fileJson=commodityName+'.json'
    with open(fileJson,'r',encoding='utf-8') as fOpen:
        dataOfBlockChain=json.load(fOpen)

    # 返回区块链状态
    statusOfBlockChain=returnBlockChainStatus(commodityName)

    # 计算每一个区块的哈希值
    for i in range(1,statusOfBlockChain+1):
        index=str(i)
        lastSecondIndex=str(i-1)

        # 如果不是第一个区块链，赋值前哈希值
        if i!=1:
            dataOfBlockChain[index]['pre_hash']=dataOfBlockChain[lastSecondIndex]['current_hash']

        # 将用作计算的信息作为一个字符串
        # dataForHash=商品名+时间+位置+用户+电话+详细描述
        dataForHash = commodityName + dataOfBlockChain[index]['infor']['event_time']
        dataForHash = dataForHash + dataOfBlockChain[index]['infor']['location']
        dataForHash = dataForHash + dataOfBlockChain[index]['infor']['person']
        dataForHash = dataForHash + dataOfBlockChain[index]['infor']['tel']
        dataForHash = dataForHash + dataOfBlockChain[index]['infor']['describe']
        output = hashCodeGenerate(dataForHash)
        # output 为返回的二元组，第一个是哈希值，第二个是随机数
        dataOfBlockChain[index]['current_hash'] = output[0]
        dataOfBlockChain[index]['random_num'] = output[1]

    # 将修改后的数据存储在对应的 .json 文件
    with open(fileJson, 'w', encoding='utf-8') as fClose:
        json.dump(dataOfBlockChain, fClose)
