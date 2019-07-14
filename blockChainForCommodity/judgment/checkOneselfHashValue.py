import json
from basicFunction.hashCodeGeneration import hashCodeGenerate
from judgment.blockChainStatus import returnBlockChainStatus

# 输入：商品名
# 结果 ：返回该区块链的 json 文件自身是否合理
def checkSelfHashValue(commodityName):

    # 检测商品状态
    statusOfCommodity=returnBlockChainStatus(commodityName)

    # 将商品信息的区块链信息从对应的 json 文件中输入
    fileName=commodityName+'.json'
    with open(fileName,'r',encoding='utf-8') as fOpen:
        blockChainData=json.load(fOpen)

    # 循环检测：
    # 1.当前区块的哈希值是否和信息的计算结果一致
    # 2.如果不是状态1，从第二个区块的前哈希值是否和前区块的哈希值一致
    for i in range(1,statusOfCommodity+1):
        index=str(i)

        # 将用作计算的信息作为一个字符串
        # dataForHash=商品名+时间+位置+用户+电话+详细描述
        dataForHash = commodityName + blockChainData[index]['infor']['event_time']
        dataForHash = dataForHash + blockChainData[index]['infor']['location']
        dataForHash = dataForHash + blockChainData[index]['infor']['person']
        dataForHash = dataForHash + blockChainData[index]['infor']['tel']
        dataForHash = dataForHash + blockChainData[index]['infor']['describe']
        # 计算哈希值和随机数,并检测
        output=hashCodeGenerate(dataForHash)
        if blockChainData[index]['current_hash']!=output[0]: return False
        elif blockChainData[index]['random_num']!=output[1]: return False

        # 如果当前区块不为 1，检查区块前哈希值是否合理
        if i!=1:
            lastSecondIndex=str(i-1)
            if (blockChainData[index]['pre_hash']!=blockChainData[lastSecondIndex]['current_hash']):return False

    # 检查第一个区块的前哈希值的默认值 ’前哈希值’ 是否被篡改
    if (blockChainData['1']['pre_hash']!='前哈希值'):return False

    return True