import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# 加载 MNIST 数据集
train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
test_dataset = datasets.MNIST(root='./data', train=False, transform=transform, download=True)

train_loader = DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=64, shuffle=False)

# 定义 CNN 模型
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # 定义卷积层：输入1通道，输出32通道，卷积核大小3x3
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        # 定义卷积层：输入32通道，输出64通道，卷积核大小3x3
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        # 定义全连接层
        self.fc1 = nn.Linear(64 * 7 * 7, 128)   # 输入大小 = 特征图大小 * 通道数
        self.fc2 = nn.Linear(128, 10)   # 10个类别

    def forward(self, x):
        x = F.relu(self.conv1(x))   # 第一层卷积 + ReLU
        x = F.max_pool2d(x, 2)      # 最大池化
        x = F.relu(self.conv2(x))   # 第二层卷积 + ReLU
        x = F.max_pool2d(x, 2)      # 最大池化
        x = x.view(-1, 64 * 7 * 7)  # 展平操作
        x = F.relu(self.fc1(x))     # 全连接层 + ReLU
        x = self.fc2(x)             # 全连接层输出
        return x

# 创建模型实例
model = SimpleCNN().to(device)

# 定义损失函数与优化器
criterion = nn.CrossEntropyLoss()   # 多分类交叉熵损失
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)    # 学习率与动量

# 训练模型
epochs = 5
model.train()   # 设为训练模式

for epoch in range(epochs):
    total_loss = 0
    for images, labels in train_loader:
        images = images.to(device)
        labels = labels.to(device)

        # 前向传播
        outputs = model(images)
        loss = criterion(outputs, labels)

        # 反向传播
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
    print(f"Epoch: {epoch + 1}  Loss: {total_loss / len(train_loader):.5f}")

model.eval()    # 设为评估模式
correct = 0
total = 0
with torch.no_grad():   # 评估时不需要计算梯度
    for images, labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)    # 预测类别
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
accuracy = 100 * correct / total
print(f"\nTest Accuracy: {accuracy:.2f}%\n")
