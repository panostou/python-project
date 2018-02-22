import random
t = []
athr=0
def BINGO(p1,length):
    succes=0
    for k in range(80):
        if succes==5:
            athr=k
            return athr
            break
        b = random.randint(1,81)
        print (b)
        for i in range(100):
            for j in range(5):
                if p1[i][j] == b:
                    p1[i][j]=0


        for i in range(100):
            succes = 0
            for j in range(5):
                if p1[i][j]==0:
                    succes +=1
            if succes == 5:
                print ("BINGO player no:", i+1, "won in", k+1,'turns')
                break

for h in range(1000):
    p1 = []
    for i in range(100):
        p2 =[]
        for j in range(5):
            p2 = random.sample(range(1,81), 5)
            p1.append(p2)

    length = len(p1)
    a=BINGO(p1,length)
    t.append(a)
for g in range (1000):
    athr= athr + t[g]
mo=(athr/1000)
print ('Ο μέσος όρος των 1000 παιχνιδίων είναι :',mo)
