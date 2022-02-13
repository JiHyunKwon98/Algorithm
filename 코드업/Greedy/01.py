# 최소대금
pasta = []
p = 3

juice = []
j = 2

for i in range(p):
    pasta.append(int(input()))

pasta_min = min(pasta)

for i in range(2):
    juice.append(int(input()))

juice_min = min(juice)

result = (pasta_min + juice_min) * 1.1

result_cal = round(result, 2)

print(result_cal)
