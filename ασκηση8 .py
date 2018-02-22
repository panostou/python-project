import random
def apotelesmata(list1,l):

    f = 0
    for i in range(0,len(list1)-2):
        sum = list1[i]
        for j in range(i+1,len(list1)-1):
            for h in range(j+1,len(list1)):
                if (list1[i] + list1[j] + list1[h] == 0):
                    print(list1[i],list1[j],list1[h])
                    f = 1

    if (f == 0):
        print("it does not exist")

list1 = random.sample(range(-30,30),30)
length = len(list1)
print(list1)
apotelesmata(list1,length)
