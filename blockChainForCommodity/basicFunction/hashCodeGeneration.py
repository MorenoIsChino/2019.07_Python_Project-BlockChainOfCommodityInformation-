import hashlib

# 输入：用来计算的数据
# 输出：返回一个元组，第一个为哈希值，第二个为随机数
def hashCodeGenerate(data):
    nonce = 0
    target = False
# 生成哈希码
    while target == False:
        # Ready for this loop
        nonce = nonce + 1
        information_01 = data
        strNonce = str(nonce)

        information_01 = strNonce + information_01
        information_01 = information_01.encode("utf-8")
        hashvalue = hashlib.sha256(information_01)
        hashCode = hashvalue.hexdigest()
        # print("test ",nonce,": ",keyval)
        # 检测哈希值是否前4位为0
        if hashCode[0:4] == "0000":
            currentHashValue = hashCode
            target = True
# 将哈希码和随机数作为一个 tuple 返回
    return hashCode,nonce