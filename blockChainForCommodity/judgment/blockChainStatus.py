import json

# 返回商品当前的状态
# 输入：商品名
# 输出：商品区块链对应的所处阶段
def returnBlockChainStatus(commodityName):
    # 添加后缀名，打开商品名对应的区块链 .json 文件
    fileName=commodityName+'.json'
    with open(fileName,'r',encoding='utf-8') as fToOpen:
        dataOfBlockChain=json.load(fToOpen)

    # 输出区块链长度作为当前状态
    status=len(dataOfBlockChain)
    return status
