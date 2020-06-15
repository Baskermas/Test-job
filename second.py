read = open('/names.txt')
capacity_temporary = []
capacity = []
sum_end  = []
max_sum = []
for i in read:
        capacity_temporary = i.split(',')
read.close()

for i in capacity_temporary:
    capacity += [(i[1:-1])]
capacity.sort()
for i in capacity:
    summ = 0
    for j in i:
        summ += ord(j) - 64
    sum_end += [summ]
for i in sum_end:
    max_sum += [i * (sum_end.index(i) +1)]
print(sum(max_sum))
# 58003822 - Ответ на 4 пункт







