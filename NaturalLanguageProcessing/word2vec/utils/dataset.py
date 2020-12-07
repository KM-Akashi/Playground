import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import collections
import random


class Corpus(torch.utils.data.Dataset):
    def __init__(self, file_path, window_size, min_frequency=0):
        super(Corpus, self).__init__()
        with open(file_path, 'r') as f:
            lines = f.readlines()
            raw_dataset = [st.split() for st in lines]

        # token-index
        counter = collections.Counter(
            [tk for st in raw_dataset for tk in st])
        self.counter = dict(
            filter(lambda x: x[1] >= min_frequency, counter.items()))

        self.idx_to_token = [
            tk for tk, _ in counter.items()
        ]
        self.token_to_idx = {
            tk: idx for idx, tk in enumerate(self.idx_to_token)
        }
        self.dataset = [[
            self.token_to_idx[tk] for tk in st if tk in self.token_to_idx
        ] for st in raw_dataset]

        # 二次采样
        # self.dataset = [
        #     [tk for tk in st if not self.discard(tk)] for st in self.dataset
        # ]
        self.num_tokens = sum([len(st) for st in self.dataset])
        # 生成中心词
        self.context_pairs = dict()
        for st in self.dataset:
            for index, tk in enumerate(st):
                lower_bound = index - window_size
                lower_bound = 0 if lower_bound < 0 else lower_bound
                upper_bound = index + window_size
                upper_bound = len(st) if upper_bound > len(st) else upper_bound

                context_words = list()
                for context_index, context_tk in \
                        zip(range(lower_bound, upper_bound+1),
                            st[lower_bound:upper_bound+1]):
                    if context_index == index:
                        continue
                    else:
                        context_words.append(context_tk)
                if tk in self.context_pairs:
                    self.context_pairs[tk].extend(context_words)
                else:
                    self.context_pairs[tk] = context_words

        self.sample = [
            [k, v] for k in self.context_pairs for v in self.context_pairs[k]
        ]

    def discard(self, idx):
        return random.uniform(0, 1) < 1 - (1e-4 / self.counter[self.idx_to_token[idx]] * self.num_tokens) ** (1/2)

    def neg_sample(self, center_word):
        ignore_list = list(
            self.context_pairs[int(center_word)])
        ignore_list.append(center_word)
        neg_words = random.choices(
            [self.token_to_idx[word]
             for word in self.idx_to_token if word not in ignore_list],
            weights=[(self.counter[word]/self.num_tokens) ** 0.75
                     for word in self.idx_to_token if word not in ignore_list],
            k=1
        )
        return neg_words[0]

    def __getitem__(self, index):
        return self.sample[index][0], self.sample[index][1], self.neg_sample(self.sample[index][0])

    def __len__(self):
        return len(self.sample)
