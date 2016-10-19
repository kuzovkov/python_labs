#Кузовков Александр Владимирович

import time
import random

n1=range(10000)
n2=range(12000)

list1=[]
for i in n1:
    list1.append(random.randrange(1,50,1))


list2=[]
for i in n2:
    list2.append(random.randrange(1,50,1))


cor1=tuple(list1)
cor2=tuple(list2)



#1
print "1 -for"

#print list1
#print list2

start=time.clock()

for item2 in list2:
    flag=False
    for item1 in list1:
        
        if item1==item2:
            flag=True

    if flag ==False:
        list1.append(item2)




end=time.clock()

#print list1
print 'Time: %s'%(end-start)


#2
print "2 - in"


list1=list(cor1)
#print list1
#print list2

start=time.clock()

for item2 in list2:
    if item2 not in list1:
        list1.append(item2)
        
 

end=time.clock()

#print list1
print 'Time: %s'%(end-start)


#3
print "3 - dict"

list1=list(cor1)
#print list1
#print list2



d1=dict(zip(list1,range(len(list1))))


start=time.clock()

for item2 in list2:
    if not d1.has_key(item2):
        list1.append(item2)


end=time.clock()

#print list1
print 'Time: %s'%(end-start)


#4
print "4 - set"

list1=list(cor1)
#print list1
#print list2

set1=set(list1)

start=time.clock()

for item2 in list2:
    if item2 not in set1:
        list1.append(item2)
    

end=time.clock()

#print list1
print 'Time: %s'%(end-start)

