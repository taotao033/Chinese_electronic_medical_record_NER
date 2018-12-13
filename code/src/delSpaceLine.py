#!bin/bash
#目的是去掉文本中空行
"""
f_in = open("../data/result/入院记录现病史/cat_valid_result.txt","r")
f_out = open("../data/result/入院记录现病史/cat_valid_result2.txt","w")
line = f_in.readline()
while line:
    line = f_in.readline()
    if line.split():
       f_out.writelines(line)
f_in.close()
f_out.close()
"""

f_in = open("../data/result/入院记录现病史/test/test.txt","r")
f_out = open("../data/result/入院记录现病史/test/test2.txt","w")
line = f_in.readline()
while line:
    line = f_in.readline()
    if line.split():
       f_out.writelines(line)
f_in.close()
f_out.close()
print("Empty lines have been deleted !")
