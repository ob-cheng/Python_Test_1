import it as it

for i in range(8):
    print(i)

print('-----------------')
for i in range(3, 8):
    print(i)

print('----------------')
for i in range(3,8):
    if i==5:
        continue
    if i==6:
        break
    print(i)