# PCA是一种降维技术，通过线性变换将数据转换到新的坐标系中，使得大部分的方差集中在前几个主成分上

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target


pca = PCA(n_components=2)   # 指定降维到二维
X_pca = pca.fit_transform(X)
# X.shape从(150, 4)变为(150, 2)


plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.title('PCA of Iris Dataset')
#plt.show()