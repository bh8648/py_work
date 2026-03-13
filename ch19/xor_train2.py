# xor_train2.py

from sklearn import svm, metrics
import pandas as pd

xor_data = [
    # P, Q, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
# 데이터 가공 - 학습을 위해 데이터와 레이블 분리
xor_df = pd.DataFrame(xor_data)

data = xor_df.iloc[:,:2]
label = xor_df.iloc[:, 2:]

print(xor_df)
print()
print(data)
print()
print(label)


clf = svm.SVC()
clf.fit(data, label)

pre = clf.predict(data)
print(f"예측결과: {pre}")

ac_score = metrics.accuracy_score(label, pre)
print(f"accuracy: {ac_score}")
