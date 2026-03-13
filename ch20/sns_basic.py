# sns_basic.py


import seaborn as sns
import matplotlib.pyplot as plt

# 데이터셋 로드
iris = sns.load_dataset("iris")
print(type(iris))
print(iris)

# 2. 기본 스타일 설정
sns.set_theme(style='whitegrid')

# 3. 그래프 표시
# sns.scatterplot(data=iris,
#                 x="sepal_length",
#                 y="sepal_width",
#                 hue="species",
#                 style='species')

# sns.lmplot(data=iris,
#                 x="sepal_length",
#                 y="sepal_width",
#                 hue="species",
#                 height=6)

# sns.histplot(data=iris,
#                 x="sepal_length",
#                 hue="species",
#                 kde=True) # kde(커널밀도추정): 분포 곡선 표시

# plt.title("Hist Plot Example")


# sns.boxplot(data=iris,
#                 x="species",
#                 y="sepal_length")

# plt.title("Box Plot Example")


sns.pairplot(data=iris,
                hue="species")

plt.title("Pair Plot Example")




plt.show()



