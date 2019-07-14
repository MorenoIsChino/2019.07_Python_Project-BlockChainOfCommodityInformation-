def generateNewBlock():
    rawDataFormat = {
        'pre_hash': '前哈希值',
        'infor':
        {
            'event_time': '时间',
            'location':'地点',
            'person': '用户名',
            'tel': '电话',
            'describe': '描述'
        },
        'current_hash': '该区块哈希值',
        'random_num': "随机数"
    }
    return rawDataFormat
