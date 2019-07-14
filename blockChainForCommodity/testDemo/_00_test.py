import json
from blockChainInformation_IO.updateLastBlockHashValue import updateLastBlockValue
from blockChainInformation_IO.addOneBlock import addOneBlockToAJsonFile
from blockChainInformation_IO.newCommodity import generateNewCommodityBlockChain

name='5'
generateNewCommodityBlockChain(name)
filename=name+'.json'
with open(filename,'r',encoding='utf-8') as f:
    data_json=json.load(f)
    print(data_json)

# 添加数据块 1
addOneBlockToAJsonFile(name,'2019.07.09','北京','Moreno','18801283107','hahahahaahahahhahahah')
# 更新最后一块区块的哈希值
updateLastBlockValue(name)
with open(filename,'r',encoding='utf-8') as f:
    data_json=json.load(f)
    print(data_json)

# 添加数据块 2
addOneBlockToAJsonFile(name,'2019.07.09','上海','Elena','18866598','uwuwuwuwuwwuuw')
# 更新最后一块区块的哈希值
updateLastBlockValue(name)
with open(filename,'r',encoding='utf-8') as f:
    data_json=json.load(f)
print(data_json)

# 添加数据块 3
addOneBlockToAJsonFile(name,'2019.07.09','广州','Ama','18297448653','sdasasasasasassa')
# 更新最后一块区块的哈希值
updateLastBlockValue(name)
with open(filename,'r',encoding='utf-8') as f:
    data_json=json.load(f)
print(data_json)

# 添加数据块 4
addOneBlockToAJsonFile(name,'2019.07.09','深圳','Elena','119','fgfgfgfgf')
# 更新最后一块区块的哈希值
updateLastBlockValue(name)
with open(filename,'r',encoding='utf-8') as f:
    data_json=json.load(f)
print(data_json)

# 添加数据块 5
addOneBlockToAJsonFile(name,'2019.07.09','兰州','Elena','110','fffedftghthtyhyj')
# 更新最后一块区块的哈希值
updateLastBlockValue(name)
with open(filename,'r',encoding='utf-8') as f:
    data_json=json.load(f)
print(data_json)


# 生成只有一个区块的区块链
name='1'
generateNewCommodityBlockChain(name)
filename=name+'.json'
with open(filename,'r',encoding='utf-8') as f:
    data_json=json.load(f)
    print(data_json)
# 添加数据块 1
addOneBlockToAJsonFile(name,'2019.07.09','北京','Moreno','18801283107','hahahahaahahahhahahah')
# 更新最后一块区块的哈希值
updateLastBlockValue(name)
with open(filename,'r',encoding='utf-8') as f:
    data_json=json.load(f)
    print(data_json)