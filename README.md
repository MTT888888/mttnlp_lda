# TextRank4ZH

TextRank算法可以用来从文本中提取关键词和摘要（重要的句子）。TextRank4ZH是针对中文文本的TextRank算法的python算法实现。

## 依赖
jieba >= 0.35  
numpy >= 1.7.1  
networkx >= 1.9.1  

## 兼容性
在Python 3.6.4中测试通过。


## 原理

TextRank的详细原理请参考：

> Mihalcea R, Tarau P. TextRank: Bringing order into texts[C]. Association for Computational Linguistics, 2004.


### 关键词提取
将原文本拆分为句子，在每个句子中过滤掉停用词（可选），并只保留指定词性的单词（可选）。由此可以得到句子的集合和单词的集合。

每个单词作为pagerank中的一个节点。设定窗口大小为k，假设一个句子依次由下面的单词组成：
```
w1, w2, w3, w4, w5, ..., wn
```
`w1, w2, ..., wk`、`w2, w3, ...,wk+1`、`w3, w4, ...,wk+2`等都是一个窗口。在一个窗口中的任两个单词对应的节点之间存在一个无向无权的边。

基于上面构成图，可以计算出每个单词节点的重要性。最重要的若干单词可以作为关键词。


### 关键短语提取
参照[关键词提取](#关键词提取)提取出若干关键词。若原文本中存在若干个关键词相邻的情况，那么这些关键词可以构成一个关键词组。

例如，在一篇介绍`支持向量机`的文章中，可以找到关键词`支持`、`向量`、`机`，通过关键词组提取，可以得到`支持向量机`。

### 摘要生成
将每个句子看成图中的一个节点，若两个句子之间有相似性，认为对应的两个节点之间有一个无向有权边，权值是相似度。

通过pagerank算法计算得到的重要性最高的若干句子可以当作摘要。


## 示例
见[Topics](../TextRank4ZH/Topics)

Topics.py:

```python
from __future__ import print_function


import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence

text = codecs.open('../Data/doc/corpus.txt', 'r', 'utf-8').read()
tr4w = TextRank4Keyword()

tr4w.analyze(text=text, lower=True, window=2)  # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象

print( '关键词：' )
for item in tr4w.get_keywords(20, word_min_len=1):
    print(item.word, item.weight)

print()
print( '关键短语：' )
for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num= 2):
    print(phrase)

tr4s = TextRank4Sentence()
tr4s.analyze(text=text, lower=True, source = 'all_filters')

print()
print( '摘要：' )
for item in tr4s.get_key_sentences(num=3):
    print(item.index, item.weight, item.sentence)  # index是语句在文本中位置，weight是权重
"""
运行结果如下：

关键词：
河南省 0.03289473058225742
教学 0.0242738644087274
纺织 0.015115404722686758
全国 0.014971416283050473
学校 0.014554063697697437
人 0.013798147764319002
获得 0.011860711808872519
学院 0.011799228092879468
竞赛 0.01161681024296488
专业 0.009265461284461938

关键短语：
学校获得
设计专业
全国高校
全国大学生

摘要：
在“2017年全国大学生电子设计竞赛”中，学校获得国家一等奖2项、二等奖6项，获奖项目数量位列河南省高校获奖第一名
在全国大学生“挑战杯”竞赛、数学建模竞赛、大学生电子设计竞赛、大学生机械创新设计大赛等国家级赛事中，中原工学院学生成绩优异，在“挑战杯”系列竞赛中共获得国家级一等奖1项、二等奖1项、三等奖13项，共荣获5次河南省“优胜杯”，国赛进步显著奖1项
目前，学校有4个国家级特色专业，1个国家级专业综合改革试点专业，1个国家级实践教学基地，1个全国高校思想政治理论课教学科研团队，还有一批省级特色专业、实验教学示范中心（实验室）、教学团队、精品资源共享课、双语教学示范课等



"""












