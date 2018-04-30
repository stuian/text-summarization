#encoding=utf-8

import mxnet as mx
from mxnet import autograd ,gluon,nd
from mxnet.gluon import nn,rnn,Block
from mxnet.contrib import text

from io import open
import collections
import datetime

PAD = '<pad>'
BOS = '<bos>'
EOS = '<eos>'

#可调节参数
epochs = 50
epoch_period = 10 # 每十次打印结果

learning_rate = 0.005

max_seq_len = 5
encoder_num_layers = 1
decoder_num_layers = 2

encoder_drop_prob = 0.1
deconder_drop_prob = 0.1

encoder_hidden_dim = 256
decoder_hidden_dim = 256
alignment_dim  = 25

# 读取数据
def read_data(max_seq_len):
    input_tokens = []
    output_tokens = []
    input_seqs = []
    output_seqs = []

    with open('../data/fr-en-small.txt') as f:
        lines = f.readlines()
        for line in lines:
            input_seq, output_seq = line.rstrip().split('\t')
            cur_input_tokens = input_seq.split(' ')
            cur_output_tokens = output_seq.split(' ')

            if len(cur_input_tokens) < max_seq_len and \
                            len(cur_output_tokens) < max_seq_len:
                input_tokens.extend(cur_input_tokens)
                # 句末附上EOS符号。
                cur_input_tokens.append(EOS)
                # 添加PAD符号使每个序列等长（长度为max_seq_len）。
                while len(cur_input_tokens) < max_seq_len:
                    cur_input_tokens.append(PAD)
                input_seqs.append(cur_input_tokens)
                output_tokens.extend(cur_output_tokens)
                cur_output_tokens.append(EOS)
                while len(cur_output_tokens) < max_seq_len:
                    cur_output_tokens.append(PAD)
                output_seqs.append(cur_output_tokens)

        fr_vocab = text.vocab.Vocabulary(collections.Counter(input_tokens),
                                         reserved_tokens=[PAD, BOS, EOS])
        en_vocab = text.vocab.Vocabulary(collections.Counter(output_tokens),
                                         reserved_tokens=[PAD, BOS, EOS])
    return fr_vocab, en_vocab, input_seqs, output_seqs

