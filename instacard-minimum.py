import time
b=[]
min='1000000000'
count=0
with open("C:\\Users\\Milad\\Downloads\\Compressed\\instacart_online_grocery_shopping_2017_05_01\\instacart_2017_05_01\\order_products__prior.csv") as prior:
    for line in prior:
        a=line.split(',')
        b.append(a[1])
with open("C:\\Users\\Milad\\Downloads\\Compressed\\instacart_online_grocery_shopping_2017_05_01\\instacart_2017_05_01\\pro.csv",encoding='utf8') as product:
    t0=time.time()
    for line in product:
        c=line.split(',')
        count+=1
        if b.count(c[0])<int(min) and count >1:
            min=b.count(c[0])
            minindx=c[0]
            minname=c[1]
    t1=time.time()
    t=t1-t0
    seconds=t%60
    minutes=(t%3600)/60
    hours=t/3600
    print ("Minimum:\nProduct No. : %s\nNumber of Orders: %d\nProduct Name: %s\nProcess Time: %d:%d:%d" % (minindx,min,minname,hours,minutes,seconds))
