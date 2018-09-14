# Convolutional Neural Network with Word Embeddings for Chinese Word Segmentation 基于词嵌入的CNN中文分词

## Introduction

1. 背景

   + 中文的词没有明显分隔符+

     大多数NLP任务是**word-based**的

     ​——> 中文分词(Chinese word segmentation, CWS)很重要

   + CWS 被视为**character-based**的序列标记任务

2. 传统序列标记任务

   + Linear models: Maximum Entropy (ME), Conditional Random Fields (CRF)

     ​	缺点：严重依赖于人工选择feature(一个字算基本单位，两个字算基本单位？)

   + 使用NN

     ​	特点：自动学习internal representations (feature?)

3. NN应用到CWS中有多个尝试，仅仅是NN结构有所不同

   + feed-forward neural network (Zheng et al., 2013)
   + tensor neural network (Pei et al., 2014), 
   + recursive neural network (Chen et al., 2015a), 
   + long-short term memory (LSTM) (Chen et al., 2015b), 
   + combination of LSTM and recursive neural network (Xu and Sun, 2016)

   它们都是将input character sequences变为contextual representations，再输入到a prediction layer

   缺点：

   1. 不能很好地自动捕捉n-gram features，不能很好地发挥NN的强项

      解法：character-based CNN (之前全是ffNN或RNN CNN善于捕捉n-gram)

      input character sequences —>(stacked convolutional layers)—>contextual representations

      —>sequence-level prediction (CRF layer 条件随机场)

   2. 没有完全地使用word信息

      解法：之前有人验证了word embedding 对于 word-based CWS很有效，但是很难用于character-based CWS. 这里提出了一种使用word embedding的方法，将word embedding 在large auto-segmented data上学习。因此这种方法属于半监督学习 (喵喵喵？)

4. benchmark

   PKU 和 MSR



## Architecture

顺序：底层到上层

1. Lookup Table

   用途：words/characters —> embeddings (词向量？)

   方法：characters lookup table. |V~char~|(char表大小)×d(dim of embeddings)

   ​	    a sentence S = (c~1~ , c~2~, ..., c~L~) —> X ∈ R^L×d^ 注意L对应的两个位置

   输出：多个char vector的相接 L*d

2. Convolutional Layer

   用CNN来encode contextual information. (char-level CNN) CNN被证明可以自动学会区分不同类的n-grams 如prefix, suffixes等

   结构：仅卷积层们，没有pooling layer。用的是GLU(gated linear unit), 在ML任务重比rectiﬁed linear unit (ReLU)好。

   输出：L*C (C是label数量)

   这里再加点东西！

3. CRF Layer

   求score, cost function之类的



## Integration with Word Embeddings

Character-based CWS 灵活高效，但是难纳入full word information。这时可以用word-level，不仅利用character-level, 还利用word-level。

我们的方法：word embedding + our characterbased model

两个优点：

1. full word information can be used.
2. large unlabeled data can be better exploited.

使用方法：

​	We associate to the word features a lookup table M~word~ 

公式：看原文。

出现的问题：feature space太大，需要shrink

​	解法：去掉低频词，用UNK代替



## Experiments



















