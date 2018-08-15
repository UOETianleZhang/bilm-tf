import argparse
import os
from collections import Counter
import nltk

def main(args):
    path = args.path

    counter = Counter()
    # path = "D:/Python34/news"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    s = []
    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            f = open(path + "/" + file);  # 打开文件
            iter_f = iter(f);  # 创建迭代器
            # str = ""
            for line in iter_f:  # 遍历文件，一行行遍历，读取文本
                counter.update(line.split())
    # print(s)
    #
    # fo = open("/Users/tianlezhang/PycharmProjects/tf/ELMo_tf/data/tt")
    # text = fo.read()
    # fo.close()
    # # text = 'I I love NLP la la la'


    # tokens = nltk.word_tokenize(text)
    # counter.update(tokens)
    vocab = [word for word,_ in counter.most_common(len(counter)) if counter[word] > 0]
    # vocab_fre = [word+'\t'+str(fre) for word,fre in counter.most_common(len(counter)) if counter[word] > 0]

    vocab_fre = [(word,fre) for word,fre in counter.most_common(len(counter)) if counter[word] > 0]
    fre_sum = 0
    for _,fre in vocab_fre:
        fre_sum += fre
    i = 0
    sum = 0
    print("fre_sum:\t%d" % fre_sum)
    for _,fre in vocab_fre:
        sum += fre
        if sum >= 0.95*fre_sum:
            break
        i += 1
    print("95%% n_line:%d\t" % i)

    vocab.insert(0, '<S>')
    vocab.insert(1, '</S>')
    vocab.insert(2, '<UNK>')
    vocab.insert(3, '<NUM>')
    vocab.insert(4, '<ENG>')
    vocab.insert(5, '<NUM_ENG>')
    vocab = vocab[:10000]
    print("vocab length:%d" % len(vocab))
    # word_to_ix = dict(zip(vocab, range(len(vocab))))

    with open(args.fo+'.txt','w') as fo:
        for word in vocab:
            fo.write(word+"\n")

    with open(args.fo+'_ref.txt','w') as fo_fre:
        for word,fre in vocab_fre:
            fo_fre.write(word+"\t"+str(fre)+"\n")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--path')
    parser.add_argument('--fo')
    # parser.add_argument('--vocab_file', help='Vocabulary file')
    # parser.add_argument('--train_prefix', help='Prefix for train files')

    args = parser.parse_args()
    main(args)