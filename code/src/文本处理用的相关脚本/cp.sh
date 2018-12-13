#!/bin/bash
#先拷贝 400个 原始未标注文本作为训练集
for i in {1..400}
do
  cp -f ./origin-data/入院记录现病史-$i.txtoriginal.txt ./CCKS2018/NeuroNER/data/conll2003/en/train
done
echo "400个 原始未标注文本已经拷贝到 "+"./CCKS2018/NeuroNER/data/conll2003/en/train下"
#再拷贝200个原始未标注文本作为验证集
for i in {401..600}
do
   cp -f ./origin-data/入院记录现病史-$i.txtoriginal.txt ./CCKS2018/NeuroNER/data/conll2003/en/valid
done
echo "200个 原始未标注文本已经拷贝到 "+"./CCKS2018/NeuroNER/data/conll2003/en/valid 下"
#拷贝后来组委会官方给出的的400个测试文本
for i in {1..400}
do
   cp -f ./testdata/入院记录现病史-$i.txtoriginal.txt ./CCKS2018/NeuroNER/data/conll2003/en/test
done
echo "200个 原始未标注文本已经拷贝到 "+"./CCKS2018/NeuroNER/data/conll2003/en/test 下"

