import it as it
# 'for' loops
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

print('------------------')

x=10
for i in range(1,x+1):
    print(i)

# 'while' loop
print('-----------')

a=10
for i in range(3):
    print(i)
    print(a)
    b=10
print('a=%s'%a)
print('b=%s'%b)