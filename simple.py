

import random

pc=random.randint(1,5)

print(pc)


for i in range(1,4):
    

    user=int(input())

    if(user==pc):
        print('congratulations')
        break
    elif(user>pc):
        print("user is high than pc")
        continue
    elif(user<pc):
        print("user is less than pc")
        continue
    else:
        print("invalid number")


if(i==3):
    print("game over,play again!")
    