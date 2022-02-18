import pyupbit
import numpy as np

df = pyupbit.get_ohlcv("KRW-BTC", count=7)

# 변동폭 * K = (고가 - 저가) * K값
df['range'] = (df['high'] - df['low']) * 0.5

# 매수가
df['target'] = df['open'] + df['range'].shift(1)

# 수익율
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

# 누적 수익율
df['hpr'] = df['ror'].cumprod()

# Draw down
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# MDD
print("MDD(%): ", df['dd'].max())

# 엑셀로 출력
df.to_excel("backtesting_result.xlsx")