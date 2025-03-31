from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs # 用于生成数据集
import matplotlib.pyplot as plt

# 生成一个二维数据集，包含300个样本，4个聚类中心，标准差为0.06，随机种子为0
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
# 只关心X，不关心label，所以用_忽略

# 训练K-means模型
model = KMeans(n_clusters=4)    # 指定算法聚类数为4
model.fit(X)

# 预测聚类结果
y_kmeans = model.predict(X)

# 可视化聚类结果
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
plt.show()