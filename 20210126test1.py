"""###猜数游戏，用while循环

import random

computer_number=random.randint(1,100)
while True:
    person_number=(int(input("请输入1个数字:")))
    #print(computer_number)
    if person_number>computer_number:
        print('太大了')
    elif person_number<computer_number:
        print('太小了')
    elif person_number == computer_number:
        print('猜对啦')
        break

"""

##计算1加到100
i=0
sum=0
for i in range(101):
    sum=sum+i
    i+=1
print(sum)
