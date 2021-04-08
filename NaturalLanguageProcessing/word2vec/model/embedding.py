import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


class Embedding(nn.Module):
    def __init__(self, num_embeddings, embedding_dim):
        super(Embedding, self).__init__()
        self.num_embeddings, self.embedding_dim = num_embeddings, embedding_dim
        self.embed_v = nn.Embedding(num_embeddings, embedding_dim)
        self.embed_u = nn.Embedding(num_embeddings, embedding_dim)

        torch.nn.init.normal_(self.embed_v.weight, mean=0, std=1)
        torch.nn.init.uniform_(self.embed_v.weight, -0, 0)

    def forward(self, center_word, context_word, negative_word):
        v = self.embed_v(center_word)
        u = self.embed_u(context_word)
        neg = -1 * self.embed_u(negative_word)

        pos_score = F.logsigmoid(
            torch.bmm(v, u.permute(0, 2, 1))
        )
        neg_score = F.logsigmoid(
            torch.bmm(v, neg.permute(0, 2, 1))
        )
        return -torch.mean(pos_score+neg_score)

    def predict(self, idx):
        return self.embed_v(idx)
