# iris.py

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 데이터 다운받는거 싫으니까 안함
"""
iris = load_iris()

iris.data
df = pd.Dataframe(iris.data, columns=iris.feature_names)
df['target'] = iris.target

target_names = {
    0:iris.target_names[0],
    1:iris.target_names[1],
    2:iris.target_names[2]
}

train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label, train_size=0.7)

clf = svm.SVC()
slf.fit(train_data, train_label)

pre = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_labe, pre)

print(ac_score)

"""



