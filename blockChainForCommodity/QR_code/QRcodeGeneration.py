import qrcode
import json
import os

# 输入商品名，获得名为“商品名.png”的二维码的文件路径
def generateQRcode(commodityName):
    #获取商品数据
    fileName=commodityName+'.json'
    with open(fileName,'r',encoding='utf-8') as fOpen:
        dataOfCommodity=json.load(fOpen)

    # 简化抽取区块链信息 区块1：location，tel
    simpilDataForQrcode=''
    for key in dataOfCommodity:
        simpilDataForQrcode=simpilDataForQrcode+'区块'+key+': 地点-'+dataOfCommodity[key]['infor']['location']+',tel-'+dataOfCommodity[key]['infor']['tel']+'/'
    # print(simpilDataForQrcode)

    # 获取文件夹路径
    dirPath = os.getcwd()
    fileOfQrCode=commodityName+'.png'
    # 与文件路径进行合并
    absPath=os.path.join(dirPath, fileOfQrCode)
    # print(absPath)

    img = qrcode.make(simpilDataForQrcode)
    img.save(absPath)
    # print("交易信息二维码生成成功\n存放地址：%s"% absPath)

    # 返回绝对路径
    return absPath