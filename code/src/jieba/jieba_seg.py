# encoding=utf-8
import jieba
jieba.load_userdict("../dict.txt")
#seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
#print("Full Mode: " + "/ ".join(seg_list))  # 全模式
file_input = open("../cat.txt","r").read()
file_input = ' '.join(jieba.cut(file_input))

file_output = open("./origin-data_seg.txt","w")
file_output.write(file_input)

#print (str)
#file_input.close()

#seg_list = jieba.cut(str, cut_all=False)
#print( " ".join(seg_list))  # 精确模式
#file_input.close()
#seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
#print(", ".join(seg_list))

#seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
#print(", ".join(seg_list))
