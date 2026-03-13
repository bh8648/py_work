# stats1.py

import statsmodels.api as sm

data = sm.datasets.get_rdataset("mtcars").data
print(data.head())

print(data)

X = data[['hp', 'wt']] # 마력, 중량 -> 독립변수
Y = data['mpg'] # 연비 -> 종속변수

# 상수항 추가
X = sm.add_constant(X)
print(X)

# 모델 생성 및 학습(fit)
# OLS (Ordinary Least Squares) : 오차의 제곱을 최소화하는 기울기와 절편을 찾음
model = sm.OLS(Y, X).fit()

print(model.summary())


print(model.params)
