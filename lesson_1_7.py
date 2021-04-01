# Подсчет баланса
waste = 0


def counting(day):
    global waste
    waste += day

counting(17)
counting(20)
counting(21)
print(waste)


def counting_2(*waste_1):
  sum_1 = 0
  for day in waste_1:
    sum_1 += day
  return sum_1

print(counting_2(56, 14, 17, 56))
