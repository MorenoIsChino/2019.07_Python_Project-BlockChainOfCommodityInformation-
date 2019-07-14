import json
from judgment.blockChainStatus import returnBlockChainStatus
from judgment.checkOneselfHashValue import checkSelfHashValue
def returnInforToMySQL_table(commodityName):
    MySQL_character={
        'event_name':'商品名',
        'event_time': '时间',
        'location': '地点',
        'person': '用户名',
        'tel': '电话',
        'desc': '描述',
        'random_num': "随机数",
        'current_hash': '该区块哈希值',
        'pre_hash': '前哈希值',
        'status':'区块链信息是否有效，即每一块的哈希值都合理',
        'chain_index':'区块链所属阶段'
    }

    # 打开对应商品名的 .json 数据
    fileName=commodityName+'.json'
    with open(fileName,'r',encoding='utf-8') as fOpen:
        blockChainData=json.load(fOpen)

    # 返回区块链所处状态
    blockChainStatus=returnBlockChainStatus(commodityName)
    # 最后一个区块的数据的 key
    index=str(blockChainStatus)

    # 赋值 ：商品名、区块链状态
    MySQL_character['event_name']=commodityName
    MySQL_character['chain_index']=blockChainStatus

    # 赋值：时间、地点、用户名、电话、描述
    MySQL_character['event_time']=blockChainData[index]['infor']['event_time']
    MySQL_character['location']=blockChainData[index]['infor']['location']
    MySQL_character['person']=blockChainData[index]['infor']['person']
    MySQL_character['tel']=blockChainData[index]['infor']['tel']
    MySQL_character['desc']=blockChainData[index]['infor']['describe']

    # 赋值：前哈希值，哈希值，随机数，当前区块链信息是否合理的状态
    if (checkSelfHashValue(commodityName)==True):
        # 区块链信息 合理
        MySQL_character['pre_hash'] = blockChainData[index]['pre_hash']
        MySQL_character['current_hash'] = blockChainData[index]['current_hash']
        MySQL_character['random_num'] = blockChainData[index]['random_num']
        MySQL_character['status'] = 'Y'
    elif (checkSelfHashValue(commodityName)==False):
        # 区块链信息  不合理
        MySQL_character['pre_hash'] = ''
        MySQL_character['current_hash'] = ''
        MySQL_character['random_num'] = '00000'
        MySQL_character['status'] = 'N'

    return MySQL_character