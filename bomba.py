import time

print('A bomba foi acionada e você tem 10 segundos para fugir')
for i in range(10, 0, -1):
    time.sleep(1)
    print(i)
    if(i == 1):
        time.sleep(1)
        print('Buuuuuuummm!!!')