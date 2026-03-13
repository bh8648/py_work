# sns_facetgrid.py


import seaborn as sns
import matplotlib.pyplot as plt

# 샘플데이터셋 로드
tips = sns.load_dataset("tips")
print(tips)

g = sns.FacetGrid(data=tips,
                  row="sex",
                  col="time")

# data: DF
# row: 특정 기준에 따라 행 분할
# col: 특정 기준에 따라 열 분할
# height: 각 면의 높이(인치)
# aspect: 가로, 세로 비율을 조절 -> 1.6이라면 가로:세로=1.6:1

g.map_dataframe(func=sns.scatterplot,
                x="total_bill",
                y="tip")

# func: 그래프 종류
# x축 설정

g.set_titles(row_template="{row_name}",
             col_template="{col_name}")


plt.show()
