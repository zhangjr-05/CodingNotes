import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = {
    '面积': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
    '房价': [150, 180, 200, 240, 270, 300, 320, 350, 380, 400]
}

df = pd.DataFrame(data)

X = df[['面积']]    # 这是DataFrame
y = df['房价']      # 这是Series

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=None)

# 训练线性回归模型
model = LinearRegression()
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

i = 0
while i < len(y_pred):
    square = X_test['面积'].iloc[i]
    t_pruice = y_test.iloc[i]
    p_price = y_pred[i]
    print(f'这套房面积为{square}平方米，预测房价为{p_price:.2f}万元，实际房价为{t_pruice:.2f}万元')
    i += 1
