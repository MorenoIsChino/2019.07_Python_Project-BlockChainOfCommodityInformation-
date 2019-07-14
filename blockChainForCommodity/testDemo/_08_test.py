# 测试返回给数据库的商品区块链信息
from judgment.returnInformationToSQL import returnInforToMySQL_table
from blockChainInformation_IO.editLastBlockInformation import editLastBlock

data1=returnInforToMySQL_table('1')
print('-------------------   1     ----------------')
print(data1)
print('')

data5=returnInforToMySQL_table('5')
print('-------------------   5     ----------------')
print(data5)
print('')

# 修改最后一个区块信息后再次查看
editLastBlock('1','1','1','1','1','1')
data1=returnInforToMySQL_table('1')
print('-------------------   1  changed   ----------------')
print(data1)
print('')

editLastBlock('5','1','1','1','1','1')
data1=returnInforToMySQL_table('5')
print('-------------------   5  changed   ----------------')
print(data1)
print('')