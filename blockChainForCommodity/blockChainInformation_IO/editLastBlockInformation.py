from blockChainInformation_IO.newBlock import generateNewBlock
from judgment.blockChainStatus import returnBlockChainStatus
import json

# 输入：商品名，时间，位置，用户名，电话，描述
# 结果：编辑区块链的最后一个区块的信息，但这里的最后一个区块的哈希值是无效的
# 哈希值需要用 updateLastBlockHashValue 中的函数 updateLastBlockValue（）去更新
def editLastBlock(commodityName,event_time,location,persion,tel,describe):
    # 添加后缀名，打开商品名对应的区块链 .json 文件
    fileName=commodityName+'.json'
    with open(fileName,'r',encoding='utf-8') as fToOpen:
        dataOfBlockChain=json.load(fToOpen)

    # 根据文件当前的区块链长度确定需要 编辑 的区块的 key 值
    index=str(returnBlockChainStatus(commodityName))

    # 给新的区块内容上写入有效信息
    dataOfBlockChain[index]['infor']['event_time']=event_time
    dataOfBlockChain[index]['infor']['location']=location
    dataOfBlockChain[index]['infor']['person']=persion
    dataOfBlockChain[index]['infor']['tel']=tel
    dataOfBlockChain[index]['infor']['describe']=describe

    # 数据写入完成，将信息用相同的文件名存入 .json 文件
    with open(fileName,'w',encoding='utf-8') as fToSaved:
        json.dump(dataOfBlockChain,fToSaved)


