#!/bin/bash
cp -f ./CCKS2018/data/result/入院记录现病史/1-400_train.txt ./CCKS2018/NeuroNER/data/conll2003/en/train.txt

cp -f ./CCKS2018/data/result/入院记录现病史/cat_valid_result.txt ./CCKS2018/NeuroNER/data/conll2003/en/valid.txt

cp -f ./CCKS2018/data/result/入院记录现病史/cat_test_result.txt ./CCKS2018/NeuroNER/data/conll2003/en/test.txt

echo finished 
