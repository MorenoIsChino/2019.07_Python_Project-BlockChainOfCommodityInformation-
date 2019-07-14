import json

fileName_1='1111.json'
with open(fileName_1, 'r', encoding='utf-8') as fToOpen1:
    dataOfBlockChain1 = json.load(fToOpen1)
fileName_2='2222.json'
with open(fileName_2, 'r', encoding='utf-8') as fToOpen2:
    dataOfBlockChain2 = json.load(fToOpen2)

if dataOfBlockChain1==dataOfBlockChain2:
    print('yes')
else:
    print('no')