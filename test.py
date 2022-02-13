import pyupbit

access = "YdxUmuF5UjGpOfRZ9AdPnPZ59FEYgLUwbktE6gWP"      
secret = "S0yuk0Ooc4RvJ54hviXL0jfiElLVsfmxdYlf91XV"
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BCH"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회