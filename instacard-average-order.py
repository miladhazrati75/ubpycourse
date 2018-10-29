import time
counter=0
b=[]
ordersfile=input("Please Enter orders.csv path:")
with open(ordersfile) as orders:
        a=line.split(',')
        b.append(a[5])
    t0=time.time()
    for i in range(1,24):
        counter+=b.count(str(i))
    average=counter/24
    t1=time.time()
    t=t1-t0
    seconds=t%60
    minutes=(t%3600)/60
    hours=t/3600
    print("Average Order per hours of the day: %d\nProcess Time: %d:%d:%d"% (average,hours,minutes,seconds))