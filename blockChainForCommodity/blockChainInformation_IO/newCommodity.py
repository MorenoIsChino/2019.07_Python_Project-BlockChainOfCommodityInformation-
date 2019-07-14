import json
from blockChainInformation_IO.newBlock import generateNewBlock

# 输入：商品名
# 在文件夹下生成一个名为 “商品名.json”的储存区块链信息的文件
# 在这个 .json 文件生成时它是空的，需要用 addOneBlock 下的函数 addOneBlockToAJsonFile（）来添加数据
# commodityName 是商品名，即数据库表中的 event_name
def generateNewCommodityBlockChain(commodityName):
    # 复制一个标准区块链的字典信息
    data=generateNewBlock()
    block = {}

    # 将数据储存在 .json 文件之中
    fileNameOfJsonData=commodityName+'.json'
    with open(fileNameOfJsonData,'w',encoding='utf-8') as f:
        # 参数 ：data,file*
        json.dump(block,f)


