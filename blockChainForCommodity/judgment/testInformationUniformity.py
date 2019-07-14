import json

# 输入：商品名，从其他节点传输的该商品名的 json 数据
# 输出：本地文件中的 json 数据与服务器传回的是否一致
def testUniformity(commodityName,jsonDataFromWeb):
    fileName=commodityName+'.json'
    with open(fileName,'r',encoding='utf-8') as fOpen:
        localBlockChainData=json.load(fOpen)

    if localBlockChainData==jsonDataFromWeb:return True
    else:return False