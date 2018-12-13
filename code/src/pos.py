# coding:utf-8
import add_method
import codecs
import sys
import os
import jieba
import jieba.posseg as pseg
jieba.load_userdict("../data/jieba_dict/dict.txt")
datadir = "../data/origin-data_backup"
area = ["入院记录现病史"]
class CRF_unit:
    def __init__(self):
        self.features = []

    def test_into_aline(self, filename):
        self.features = []
        sentences = add_method.ReadFileUTF8(filename);
        for sentence in sentences:
            for token in sentence:
                self.features.append(token)

    def get_posTag(self, sentence):
       # words = ' '.join(jieba.cut(sentence))
         words = pseg.cut(sentence)
         return words

    def get_token(self, filename):
       # f = open ("../data/result/" + area[0] + "/" + "1-400_train.txt","w+")
        self.features = []
        sentences = add_method.ReadFileUTF8(filename);
        for sentence in sentences:
            words = self.get_posTag(sentence)
            for w in words:
                 for token in w.word:
                   #print(token)
                    feature = [token , "O"]
                   # print(feature)
                    self.features.append(feature)
                    
 
    def read_type(self, itype):
       # itype = itype.encode('utf-8')
        if itype == "解剖部位":
            return "AnatomicSite"
        if itype == "症状描述":
            return "SymptomsDescribed"
        if itype == "独立症状":
            return "IndependentSymptoms"
        if itype == "药物":
            return "Medicine" 
        if itype == "手术":
            return "Operation"


    def get_type(self, filename):
        sentences = add_method.ReadFileUTF8(filename);
        for sentence in sentences:
            words = sentence.split()
           # print (words[-3] + words[-2])
            x = int(words[-3])
            y = int(words[-2])

            itype = self.read_type(words[-1])
            itype = str(itype)
          #  print(itype)
          #  if itype == "None":
           #    print(filename)
           #    break
            self.features[x][1] = "B-" + itype
            for j in range(x+1,y):
                self.features[j][1] = "I-" + itype



if __name__ == '__main__':
    extractor = CRF_unit()
    x = 0;
    for i in range(1,401):
        filename = datadir + '/' + area[x] + '-'+ str(i) +'.txtoriginal.txt'
        extractor.get_token(filename)
       # f = open ("../data/result/" + area[0] + "/" + "1-400_train.txt","w+")
       # f.write(features)
        filename = datadir + '/' + area[x] + '-'+ str(i) +'.txt'
        extractor.get_type(filename)

        filename = '../data' + '/result/' + area[x] + "/train/" + 'train.txt'
        add_method.AddTrain(extractor.features, filename)
    print("Path:"+ filename + '\n' + "400个train数据标注完成") 
    
    for i in range(401,451):
        filename = datadir + '/' + area[x] + '-'+ str(i) +'.txtoriginal.txt'
        extractor.get_token(filename)
        filename = datadir + '/' + area[x] + '-'+ str(i) +'.txt'
        extractor.get_type(filename)

        filename = '../data' + '/result/' + area[x] + "/valid/" + 'valid.txt'
        add_method.AddTrain(extractor.features, filename)
    print("Path:"+ filename + '\n' + "50个valid数据标注完成")
    
    for i in range(451,601):
        filename = datadir + '/' + area[x] + '-' + str(i) + '.txtoriginal.txt'
        extractor.get_token(filename)
        filename = datadir + '/' + area[x] + '-'+ str(i) +'.txt'
        extractor.get_type(filename)
                                                                   
        filename = '../data' + '/result/' + area[x] + "/test/" + 'test.txt'
        add_method.AddTrain(extractor.features, filename)
    print("Path:"+ filename + '\n' + "150个test数据标注完成")



"""    
    for i in range(401, 601):
        filename = datadir + '/'  + area[x] + '-'+ str(i) +'.txtoriginal.txt'
        extractor.test_into_aline(filename);

        filename = '../data' + '/result/' + area[x] + '/' + "valid/" + area[x] + '.valid-' + str(i) + '.txt'
	
        add_method.AddTest(extractor.features, filename)
    print("Path:"+ filename + '\n' + "200个 valid文件，格式已转换完成!")

    for i in range(1,401):
        filename = datadir + '/' + 'test1-400/' + area[x] + '-' + str(i) + '.txtoriginal.txt'
        extractor.test_into_aline(filename);
        filename = '../data' + '/result/' + area[x] + '/' + "test/" + area[x] + '.test-' + str(i) + '.txt'
        add_method.AddTest(extractor.features, filename)
    print("Path:"+ filename + '\n' + "400个 test文件，格式已转换完成!")
"""
