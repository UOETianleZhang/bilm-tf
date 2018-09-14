#Deep contextualized word representations

## Abstract

a new type of deep contextualized word representation that models both (1) complex characteristics of word use (e.g., syntax and semantics), and (2) how these uses vary across linguistic contexts (i.e., to model polysemy).



## Introduction

1. 背景：learning high quality representations can be challenging

   一个好的representation应当满足

   - Complex characteristics of word use (e.g., syntax and semantics)
   - How these uses vary across linguistic contexts (i.e., to model polysemy)

   本文介绍了一种新的deep contextualized word representation深度上下文化的词表示，不仅满足以上的条件，还可以

   - Can be easily integrated into existing models
   - Improves the state of the art in every considered case

2. 与传统方法比较

   **传统word embedding:** each token is assigned a representation that is a function of the entire input sentence.

   ​

   **本方法:** We use vectors derived from a bidirectional LSTM that is trained with a coupled language model (LM) objective on a large text corpus. For this reason, we call them ELMo (Embeddings from Language Models) representations.

   ELMo representations are deep, in the sense that they are a function of all of the **internal layers** of the biLM.

   //加个LSTM图

3. 本方法的特点

   - we learn a linear combination of the vectors stacked above each input word for each end task, which markedly improves performance over just <u>using the top LSTM layer.</u>  这个是传统word embedding 吗？(CoVe)

     使用多层的LSTM比使用最上层强（ELMo和CoVe）


   - 不同LSTM层含有不同的信息

     - the higher-level LSTM states capture context-dependent aspects of word meaning (e.g., they can be used without modiﬁcation to perform well on supervised word sense disambiguation tasks)

     - lowerlevel states model aspects of syntax (e.g., they can be used to do part-of-speech tagging). 

     - 谷歌翻译很多时候说的是人话，但是词不达意，甚至出现逻辑相反。也许就是因为缺乏对词义的理解

     - ELMo使用语法和语义线性组合非常适合结合具体的任务，因为不同任务需要不同的语义/语法比重（词性分析 情感分类 机器翻译）

       Simultaneously exposing all of these signals is highly beneﬁcial, allowing the learned models select the types of semi-supervision that are most useful for each end task.
       ​

## ELMo: Embeddings from Language Models

ELMo word representations are functions of the entire input sentence, as described in this section. They are computed on top of two-layer biLMs with character convolutions (Sec. 3.1), as a linear function of the internal network states (Sec. 3.2). This setup allows us to do semi-supervised learning, where the biLM is pretrained at a large scale (Sec. 3.4) and easily incorporated into a wide range of existing neural NLP architectures (Sec. 3.3).

1. Bidirectional language models

   - context-independent token representation x ~k~ ^LM^(via token embeddings or a CNN over characters) -> `L layers of forward LSTMs` -> At each position k, each LSTM layer outputs a context-dependent repre→sentation h k,j LM where j = 1, . . . , L. The top layer LSTM output, h k,L LM -> is used to predict the next token t k+1 with a Softmax layer.
   - 画图？

2. 一堆公式

3. 3.3 Using biLMs for supervised NLP tasks

   - typical specific task：

     ​       a sequence of tokens (t~1~ , . . . , t~N~ ) 

     —> context-independent token representation x~k~ for each token

     —>context-sensitive representation h~k~  (typically using either bidirectional RNNs, CNNs, or feed forward networks.)


   - add ELMo to the supervised model:

     ​       freeze the weights of the biLM and then concatenate the ELMo vector ELMo~k~ task with x~k~ 输入x~k~ —> [x~k~;ELMo~k~^1^]

     —> also including ELMo at the output of the task RNN 输出[h; ELMo~2~] h~k~—>[h~k~; ELMo~k~^2^]

     —> add a moderate amount of dropout to ELMo; in some cases to regularize the ELMo weights by adding λ||w||^2^ ~2~ to the loss. λ越大ELMo越接近各层的平均

4. Pre-trained bidirectional language model architecture

   J´ozefowicz et al. (2016) and Kim et al. (2015), 

   +joint training of both directions + a residual connection between LSTM layers.

   传统方法一个词对应一个词向量。本方法每个词提供三个表示方法

   ​

## Evaluation

表格



##Analysis

1. 多层比一层好

2. 不仅输入加 输出也能加

   是All of the task architectures in this paper include word embeddings only <u>as input to the lowest layer biRNN</u>. However, we ﬁnd that <u>including ELMo at the output of the biRNN in task-speciﬁc architectures</u> improves overall results for some tasks.

3. 需要上下文来解决具体词义；不同层包含不同信息

   传统：一词对一个vector

   现在：一句话输入，动态给出每个词的vector

4. sample efficiency

   只需要用少量的样本就可以训练的很好 Figure1





