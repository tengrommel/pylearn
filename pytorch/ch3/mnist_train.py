import torch
from torch import nn # 完成神经网络的工作
from torch.nn import functional as F
from torch import optim

import torchvision
from matplotlib import pyplot as plt
from utils import one_host, plot_image, plot_curve

batch_size = 512
# step1. load dataset
train_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('mnist_data',
                               train=True,
                               download=True,
                               transform=torchvision.transforms.Compose([
                                   torchvision.transforms.ToTensor(),
                                   torchvision.transforms.Normalize(
                                       (0.1307,), (0.3081,))
                               ])),
    batch_size=batch_size, shuffle=True)

test_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('mnist_data/',
                               train=False,
                               download=True,
                               transform=torchvision.transforms.Compose([
                                   torchvision.transforms.ToTensor(),
                                   torchvision.transforms.Normalize(
                                       (0.1307,), (0.3081,))
                               ])),
    batch_size=batch_size, shuffle=False)

# x, y = next(iter(train_loader))
# print(x.shape, y.shape, x.min(), x.max())
# plot_image(x, y, 'image sample')


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(28*28, 256)
        self.fc2 = nn.Linear(256, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


net = Net()
optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)
train_loss = []

# [w1, b1, w2, b2, w3, b3] 梯度计算的优化器
# 测试 训练 迭代三次
for epoch in range(3):
    for batch_idx, (x, y) in enumerate(train_loader):
        # print(x.shape, y.shape)
        # break
        x = x.view(x.size(0), 28*28)
        # => [b, 10]
        out = net(x)
        # [b, 10]
        y_onehot = one_host(y)
        loss = F.mse_loss(out, y_onehot)
        # 得到梯度 通过梯度优化器更新
        optimizer.zero_grad()
        loss.backward()
        # w' = w - lr * grad
        # 梯度清零
        optimizer.step()
        train_loss.append(loss.item())
        if batch_idx % 10 ==0:
            print(epoch, batch_idx, loss.item())

# we get optimal [w1, b1, w2, b2, w3, b3]
plot_curve(train_loss)
# 准确度的测试
total_correct = 0
for x, y in test_loader:
    x = x.view(x.size(0), 28*28)
    out = net(x)
    # out:[b, 10] => pred: [b]
    pred = out.argmax(dim=1)
    correct = pred.eq(y).sum().float().item()
    total_correct += correct

# 将正确的个数除以总个数得到正确率
total_num = len(test_loader.dataset)
acc = total_correct/total_num
print('data acc:', acc)

x, y = next(iter(test_loader))
out = net(x.view(x.size(0), 28*28))
pred = out.argmax(dim=1)
plot_image(x, pred, 'data')
