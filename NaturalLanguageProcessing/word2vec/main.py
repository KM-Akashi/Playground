from model.embedding import Embedding
from utils.dataset import SkipGram

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import matplotlib.pyplot as plt

import time

if __name__ == "__main__":
    dataset = SkipGram('data/rawdata.txt', 3)
    dataloader = torch.utils.data.DataLoader(dataset,
                                             batch_size=1024,
                                             shuffle=True)

    net = Embedding(len(dataset.idx_to_token), 2)
    optimizer = torch.optim.SGD(net.parameters(), lr=1e-1, momentum=0.9)

    MAX_EPOCH = 2500
    print('MAX_EPOCH', MAX_EPOCH)
    for epoch in range(MAX_EPOCH):
        if (epoch+1) % 100 == 1:
            start, l_sum, n = time.time(), 0.0, 0

        for center_word, context_word, negative_word in dataloader:
            optimizer.zero_grad()
            l = net(center_word.view(-1, 1),
                    context_word.view(-1, 1),
                    negative_word.view(-1, 1))
            l.backward()
            optimizer.step()
            l_sum += l.cpu().item()
            n += 1

        if (epoch+1) % 100 == 0:
            print('epoch %d, loss %.2f, time %.2fs' %
                  (epoch + 1, l_sum / n, time.time() - start))

    for index, line in enumerate(net.embed_v.weight.data):
        plt.scatter(line[0].item(), line[1].item())
        plt.text(line[0].item(), line[1].item(), dataset.idx_to_token[index])
    plt.savefig("result.png")
