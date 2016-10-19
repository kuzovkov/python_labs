import mymod
#аргументы по умолчанию
# статическая и нестатическая переменная l
def f(a,l=[]):
    l.append(a)
    return l

print f(1)
print f("a")
print f(6)


def f2(a,l=None):
    if l==None:
        l=[]
        l.append(a)
    return l

print f2(1)
print f2("qw")
print f2(78)

#переменное число аргументов

def example(param1,*param2,**param3):
    print param1
    print "-"*60
    for i in param2:    print i
    print "-"*60
    for k in param3.keys():
        print k,":",param3[k]


#запись строки в файл
f=file("test.txt","a+")
file.write(f,"hello\n")
f.close

example ('hello',21,22,23,param31='yes',param32=32)
#print file.__doc__
#print file.write.__doc__

print file.read.__doc__


f=file("test.txt","r")
str1=file.read(f)
print "str1=",str1

str2=f.read()
print "str2=",str2

print "куб числа 3 равен: ",mymod.kub(3)




