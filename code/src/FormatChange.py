#!bin/bash
file_in = open("../data/result/入院记录现病史/train/train.txt" , "r")
file_out = open("../data/result/入院记录现病史/ultimate_data/train.txt" , "a") #打开一个文件用于追加
for line in file_in.readlines():    #依次读取每行
   # line = line.strip()      #去掉每行头尾空白
   # print(line)
    list = line.split()      #以空格隔开
   # print(list[-1])
    file_out.write(list[0] + " " + "AA" + " " + "BB" + " " + list[-1] + "\n")
file_in.close()
file_out.close()
print("train.txt's format has been converted. ")

file_in = open("../data/result/入院记录现病史/valid/valid.txt" , "r")
file_out = open("../data/result/入院记录现病史/ultimate_data/valid.txt" , "a") #打开一个文件用于追加
for line in file_in.readlines():    #依次读取每行
   # line = line.strip()      #去掉每行头尾空白
    list2 = line.split()      #以空格隔开
   # print(list[1])
    file_out.write(list2[0] + " " + "AA" + " " + "BB" + " " + list2[-1] + "\n")
file_in.close()
file_out.close()
print("valid.txt's format has been converted.")

file_in = open("../data/result/入院记录现病史/test/test.txt" , "r")
file_out = open("../data/result/入院记录现病史/ultimate_data//test.txt" , "a") #打开一个文件用于追加
for line in file_in.readlines():    #依次读取每行
   # line = line.strip()      #去掉每行头尾空白
    list3 = line.split()      #以空格隔开
    file_out.write(list3[0] + " " + "AA" + " " + "BB" + " " + list3[-1] + "\n")
file_in.close()
file_out.close()
print("test.txt format has been converted.")
