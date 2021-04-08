import torch
import collections


class MyDataset(torch.utils.data.Dataset):
    def __init__(self):
        super(MyDataset, self).__init__()
        DATA = torch.Tensor([
            [0, 0, 0],
            [1, 0, 1],
            [0, 1, 1],
            [1, 1, 0],
        ])
        self.X = DATA[:, :2]
        self.Y = DATA[:, 2].long()
        self.lens = len(DATA)

    def __getitem__(self, index):
        return self.X[index], self.Y[index]

    def __len__(self):
        return self.lens


dataloader = torch.utils.data.DataLoader(
    MyDataset(), batch_size=1, shuffle=False)


class XORNet(torch.nn.Module):
    def __init__(self, input_number, hidden_number, output_number):
        super(XORNet, self).__init__()
        self.layer = torch.nn.Sequential(
            collections.OrderedDict(
                [
                    ("linear1", torch.nn.Linear(input_number, hidden_number)),
                    ("sigmoid1", torch.nn.Sigmoid()),
                    ("linear2", torch.nn.Linear(hidden_number, output_number)),
                ]
            )
        )

    def forward(self, x):
        return self.layer(x)


net = XORNet(2, 2, 2)
loss = torch.nn.CrossEntropyLoss()
# About CrossEntropyLoss:
#   from torch.autograd import Variable
#   criterion = nn.CrossEntropyLoss()
#   output = Variable(torch.randn(10, 120).float())
#   target = Variable(torch.FloatTensor(10).uniform_(0, 120).long())
#   loss = criterion(output, target)
optimizer = torch.optim.SGD(net.parameters(), lr=1e-2, momentum=0.9)

epochs = 2000
for epoch in range(epochs):
    for x, y in dataloader:
        l = loss(net(x), y)
        optimizer.zero_grad()
        l.backward()
        optimizer.step()
    if (epoch+1) % 100 == 0:
        print('epoch %d, loss: %f' % (epoch+1, l.item()))

for x, y in dataloader:
    print(x, net(x))
