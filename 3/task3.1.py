#Кузовков Александр Владимирович

import time

list1=range(12,20000,2)
list2=range(10,30000,3)

start=time.clock()
list3=list1+list2
list3.sort()

end=time.clock()


#print list1
#print list2
#print list3

print 'Time: %s'%(end-start)


start=time.clock()


list4=[]
i=0
j=0
len1=len(list1)
len2=len(list2)

while (i<len1 and j<len2):
    if list1[i]>=list2[j]:
        list4.append(list2[j])
        j=j+1
    else:
        list4.append(list1[i])
        i=i+1

if i==len1:
    list4=list4+list2[j:]
if j==len2:
    list4=list4+list1[i:]

end=time.clock()

print 'Time: %s'%(end-start)
#print list4

