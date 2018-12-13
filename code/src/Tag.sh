#!/bin/bash

#for i in {401..600}
#do
#   crf_test -m ../data/result/入院记录现病史/crf_model_1-400train ../data/result/入院记录现病史/valid/入院记录现病史.valid-$i.txt > ../data/result/入院记录现病史/valid_result/入院记录现病史.valid_result-$i.txt
#done

for i in {1..400}
do
   crf_test -m ../data/result/入院记录现病史/train/crf_model ../data/result/入院记录现病史/test2/入院记录现病史.test-$i.txt > ../data/result/入院记录现病史/test2_tag_result/入院记录现病史.test_result-$i.txt
done
echo "finished"
