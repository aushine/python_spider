'''
or i in range(1, 101):
    if i % 2 == 0:
        continue
    print(i)
for i in range(2,100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        '''
'''
k = 1
i = 0
x = 0
while i < 5:
    x = k * 4
    for i in range(5):
        if x % 4 != 0:
            break
        i += 1
        x = (x/4) * 5 + 1
    k += 1
print(x)'''
