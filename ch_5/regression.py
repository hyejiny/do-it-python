import statsmodels.formula.api as smf
import pandas as pd

df2 = pd.read_csv('survey.csv')

# print(df2.head())

# df2에 회귀 분석 모델을 적용해 model 객체에 저장한다.
model = smf.ols(formula='jobSatisfaction~English', data=df2)

# fit함수를 이용해서 model 객체에서 결괏값을 가져온다
result = model.fit()
# print(result.summary())

# 다중 회귀 분석
model2 = smf.ols(formula='jobSatisfaction~English+stress+income', data=df2)
result2 = model2.fit()
print(result2.summary())