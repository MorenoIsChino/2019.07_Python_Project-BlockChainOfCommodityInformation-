# 测试 testUniformity（）
from judgment.testInformationUniformity import testUniformity
import json

fileName = '1111' + '.json'
with open(fileName, 'r', encoding='utf-8') as fOpen:
    webData = json.load(fOpen)

print(testUniformity('1111',webData))