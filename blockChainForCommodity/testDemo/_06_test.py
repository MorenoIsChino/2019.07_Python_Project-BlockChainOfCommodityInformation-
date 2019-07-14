from blockChainInformation_IO.editLastBlockInformation import editLastBlock
from blockChainInformation_IO.updateAllBlockHashCode import updateAllHashCode
from judgment.checkOneselfHashValue import checkSelfHashValue

# 修改商品 ‘2222’的最后一个区块的信息
editLastBlock('2222','可乐','NewYork','aaa','18890765543','desdesdes')

# 检测刚才修改的商品自身哈希值是否合理
# 预期结果：False
print(checkSelfHashValue('2222'))

# 更新最后一个区块的哈希值
# 再次检测刚才修改的商品自身哈希值是否合理
# 预期结果： True
updateAllHashCode('2222')
print(checkSelfHashValue('2222'))
