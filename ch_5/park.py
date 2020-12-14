import numpy as np

# 1,2년차에 발생한 비용
loss = [-750,-250]

# 3년차부터 발생한 이익
profit = [100] * 18

# 총 20년 동안의 현금 흐름 리스트
cf = loss + profit

# cf를 배열로 만들어 cashflow에 저장

cashflow = np.array(cf)
# print(cashflow)

# 순현재가치
npv = np.npv(0.045, cashflow)
# print(npv)

# 내부 수익률
irr = np.irr(cashflow)
print(irr)