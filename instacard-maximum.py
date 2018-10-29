import time
b=[]
max='0'
count=0
proprior=input("Please Enter order_products__prior.csv path:")
products=input("Please Enter products.csv path:")
with open(proprior) as prior:
    for line in prior:
        a=line.split(',')
        b.append(a[1])
with open(products,encoding='utf8') as product:
    t0=time.time()
    for line in product:
        c=line.split(',')
        count+=1
        if b.count(c[0])>int(max) and count >1:
            max =b.count(c[0])
            maxindx=c[0]
            maxname=c[1]
    t1=time.time()
    t=t1-t0
    seconds=t%60
    minutes=(t%3600)/60
    hours=t/3600
    print ("Maximum:\nProduct No. : %s\nNumber of Orders: %d\nProduct Name: %s\nProcess Time: %d:%d:%d" % (maxindx,max,maxname,hours,minutes,seconds))
