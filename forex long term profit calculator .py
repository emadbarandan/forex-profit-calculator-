import random 
#emad barandan
m=input('please enter yore balance ')
m=int(m)
a=random.randint(-2,1)
r=input('please enter yore risk (example = 2) ')
r=float(r)
for i in range(1,10):

    
    for j in range (1,400):
        if a>=0:
            m = m+2*m*(r/100)
        else :
            m=m-m*(r/100)
        a=random.randint(-2,1)
    print ('for round ',i,' your profit = ',m)
    print ('for calculate another round ')
    m=input('please enter yore balance ')
    m=int(m)