anak1 = 'One'
anak2 = 'Two'
anak3 = 'Three'

anak = [anak1, anak2, anak3]
print(anak)
anak.append("Add New")
print(anak)

print(f'Hai {anak[1]}')
print('--------')
for x in anak:
    print(f'{x}.Hai {x}')

print('--------')
for y in range(0, len(anak)):
    print(f'{y + 1}. hei {y}')
