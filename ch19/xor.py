# xor.py

from sklearn import svm, metrics

clf = svm.SVC()
# fit(학습데이터, 정답데이터)
clf.fit(
    [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1],
    ],
    [0,1,1,0]
)

print(clf.get_params())

pre = clf.predict(
    [
        [0,1],
        [1,1]
    ]
)

ac = metrics.accuracy_score([1,0], pre)
metrics.precision_score()
metrics.recall_score()

print(f"accuracy: {ac}")


# 커널 -> 데이터를 더 높은 차원으로 보냈다고 생각하면 거기서는 선형으로 나눌 수 있게 만들기
"""
1) Linear Kernel
그냥 선형 분류기
데이터가 거의 직선으로 나뉠 때 적합
빠르고 해석도 쉬움

2) Polynomial Kernel
다항식 형태의 경계
곡선 형태 분리가 가능

3) RBF Kernel
가장 많이 쓰이는 편
복잡한 비선형 경계를 만들 수 있음
실무에서 기본 선택으로 자주 사용
"""