#Кузовков Александр Владимирович

import time
import random

n1=range(10000)
n2=range(12000)

list1=[]
for i in n1:
    list1.append(random.randrange(1,50,1))


list2=[]
for i in n1:
    list2.append(random.randrange(1,50,1))





#1
print "1 -for"

#print list1
#print list2

start=time.clock()

list3=[]
for item1 in list1:
    flag=False
    for item3 in list3:
        
        if item1==item3:
            flag=True

    if flag ==False:
        list3.append(item1)

for item2 in list2:
    flag=False
    for item3 in list3:
        
        if item2==item3:
            flag=True

    if flag ==False:
        list3.append(item2)


end=time.clock()

#print list3
print 'Time: %s'%(end-start)


#2
print "2 -in"


start=time.clock()

list3=[]
for item1 in list1:
    if item1 not in list3:
        list3.append(item1)
        
for item2 in list2:
    if item2 not in list3:
        list3.append(item2)   

end=time.clock()

#print list3
print 'Time: %s'%(end-start)


#3
print "3 - dict"


d3={}

start=time.clock()
list3=[]
for item1 in list1:
    if not d3.has_key(item1):
        list3.append(item1)
        d3.update({item1:0})

for item2 in list2:
    if not d3.has_key(item2):
        list3.append(item2)
        d3.update({item2:0})

end=time.clock()

#print d3
#print list3
print 'Time: %s'%(end-start)

#4
print "4 - set"


start=time.clock()

list3=list(set(list1+list2))
        
    

end=time.clock()

#print list3
print 'Time: %s'%(end-start)
