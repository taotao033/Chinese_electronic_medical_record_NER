import sys
path = "./cat2.txt"   #数据来源
f = open(path , 'r')
line = f.readline()
list = []
while line:
    a = line.split()
#    print(a[0])
    b = a[0]
    list.append(b)
    line = f.readline()
f.close
list.reverse()#反向列表中元素
#print(list) 
f2 = open('dict.txt', 'w')     #提取后的数据文件
count = len(list)
while count > 0:
  f2.write(list[count - 1]+"\n")
  count = count - 1 
f2.close()

