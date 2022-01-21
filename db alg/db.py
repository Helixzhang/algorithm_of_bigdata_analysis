import xlrd
import numpy as np

def read_xlsx(filename: str):
    import os
    array = []
    data = xlrd.open_workbook(os.path.split(os.path.realpath(__file__))[0]+'/'+filename)
    table = data.sheet_by_index(0)

    for i in range(table.nrows):
        line=table.row_values(i)
        array.append(line)
    array = np.array(array)

    array = np.delete(array,(0),axis=0)
    return array.astype(np.float16)

def distance(point_A,point_B):
    assert len(point_A) == len(point_B),"向量长度不等"
    return np.linalg.norm(point_A - point_B)

data = read_xlsx('data.xls')
n = len(data)
dis = np.empty((n,n))
for i in range(n):
    for j in range(n):
        # dis[i][j] = distance(data[i].astype(np.float16),data[j].astype(np.float16))
        dis[i][j] = distance(data[i],data[j])

# print(dis>1)
dis_list = dis.flatten().tolist()
dis_list = [x for x in dis_list if x != 0.0]
dis_list.sort()

p=0.05

index = int(len(dis_list)*(1-p))-1
D = 500**(1/2)

x = 1
for row in dis:
    if np.count_nonzero(row > D)>(1-p)*n-1:print(x)
    x+=1