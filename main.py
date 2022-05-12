def importDataforPractice(file_path): #导入训练样本
    dic = {}
    with open(file_path) as file_obj:
        for line in file_obj:
            if dic.__contains__(tuple(line.split())):
                dic[tuple(tuple(line.split()))] += 1
            else:
                dic[tuple(tuple(line.split()))] = 1
    return dic

def caculateY(y,dic): #计算样本中是或否的数量
    result = 0
    for key in dic:
        if key[6] == y:
            result += 1
    return result

def caculateXY(x,i,y,dic): #计算样本中第i个特征为x且组别为y的数量
    result = 0
    for key in dic:
        if key[i] == x and key[6] == y:
            result += 1
    return result

def probability(x,i,y,dic): #计算概率
    result = caculateXY(x,i,y,dic)/caculateY(y,dic)
    return result

if __name__ == '__main__':
    result = 1
    result2 = 1
    data = importDataforPractice('样本.txt')
    sum = caculateY('是',data) + caculateY('否',data)
    with open('测试样本.txt') as file_obj:
        for line in file_obj:
            certificator = line.split()
    for i in range(len(certificator)):
        result = result * probability(certificator[i],i,'是',data)
        result2 = result2 * probability(certificator[i], i, '否', data)
    if result*(caculateY('是',data)/sum) > result2* (caculateY('否', data) / sum):
        print('是')
    else:
        print('否')



