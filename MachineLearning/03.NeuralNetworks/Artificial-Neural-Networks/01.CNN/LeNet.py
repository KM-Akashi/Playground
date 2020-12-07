import torch
import torchvision
import time


class LeNet(torch.nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        self.conv = torch.nn.Sequential(
            torch.nn.Conv2d(1, 6, 5),  # in_channels, out_channels, kernel_size
            torch.nn.Sigmoid(),
            torch.nn.MaxPool2d(2, 2),  # kernel_size, stride
            torch.nn.Conv2d(6, 16, 5),
            torch.nn.Sigmoid(),
            torch.nn.MaxPool2d(2, 2)
        )
        self.fc = torch.nn.Sequential(
            torch.nn.Linear(16*4*4, 120),
            torch.nn.Sigmoid(),
            torch.nn.Linear(120, 84),
            torch.nn.Sigmoid(),
            torch.nn.Linear(84, 10)
        )

    def forward(self, img):
        feature = self.conv(img)
        output = self.fc(feature.view(img.shape[0], -1))
        return output


if __name__ == "__main__":
    batch_size = 4096
    num_workers = 4

    mnist_train = torchvision.datasets.FashionMNIST(
        root='./data', train=True, download=True, transform=torchvision.transforms.ToTensor())
    mnist_test = torchvision.datasets.FashionMNIST(
        root='./data', train=False, download=True, transform=torchvision.transforms.ToTensor())
    train_iter = torch.utils.data.DataLoader(
        mnist_train, batch_size=batch_size, shuffle=True, num_workers=num_workers)
    test_iter = torch.utils.data.DataLoader(
        mnist_test, batch_size=batch_size, shuffle=False, num_workers=num_workers)

    # start = time.time()
    # for X, y in train_iter:
    #     continue
    # print('%.2f sec' % (time.time() - start))

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    net = LeNet().to(device)
    loss = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(net.parameters(), lr=1e-2)

    num_epochs = 100

    for epoch in range(num_epochs):
        train_l_sum, train_acc_sum, n, batch_count, start = 0.0, 0.0, 0, 0, time.time()
        for X, y in train_iter:
            X = X.to(device)
            y = y.to(device)
            y_hat = net(X)
            l = loss(y_hat, y)
            optimizer.zero_grad()
            l.backward()
            optimizer.step()
            train_l_sum += l.cpu().item()
            train_acc_sum += (y_hat.argmax(dim=1) == y).sum().cpu().item()
            n += y.shape[0]
            batch_count += 1
        print('epoch %d, loss %.4f, train acc %.3f, time %.1f sec'
              % (epoch + 1, train_l_sum / batch_count, train_acc_sum / n, time.time() - start))
