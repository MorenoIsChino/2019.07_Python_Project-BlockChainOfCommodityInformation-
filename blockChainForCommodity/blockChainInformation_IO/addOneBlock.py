from blockChainInformation_IO.newBlock import generateNewBlock
import json

# 输入：商品名，时间，位置，用户名，电话，描述
# 结果：给该商品的区块链信息添加下一阶段，但这里所添加的最后一个区块的哈希值是无效的
# 哈希值需要用 updateLastBlockHashValue 中的函数 updateLastBlockValue（）去更新
def addOneBlockToAJsonFile(commodityName,event_time,location,persion,tel,describe):
    # 添加后缀名，打开商品名对应的区块链 .json 文件
    fileName=commodityName+'.json'
    with open(fileName,'r',encoding='utf-8') as fToOpen:
        dataOfBlockChain=json.load(fToOpen)

    # 根据文件当前的区块链长度确定需要添加的区块的 key 值
    statusOfBlockChain=len(dataOfBlockChain)
    nextIndex=str(statusOfBlockChain+1)

    # 新生成一个原始区块数据，并且写入区块链的临时数据
    newBlockData=generateNewBlock()
    dataOfBlockChain[nextIndex]=newBlockData

    # 给新的区块内容上写入有效信息
    dataOfBlockChain[nextIndex]['infor']['event_time']=event_time
    dataOfBlockChain[nextIndex]['infor']['location']=location
    dataOfBlockChain[nextIndex]['infor']['person']=persion
    dataOfBlockChain[nextIndex]['infor']['tel']=tel
    dataOfBlockChain[nextIndex]['infor']['describe']=describe

    # 数据写入完成，将信息用相同的文件名存入 .json 文件
    with open(fileName,'w',encoding='utf-8') as fToSaved:
        json.dump(dataOfBlockChain,fToSaved)


