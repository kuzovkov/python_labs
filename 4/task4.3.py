#�������� ��������� ������������

ls1=range(1,10)

#1
print "#1"
print "���������� ����� � ������ �������"
print ls1
print map(lambda x:x*x*x,ls1)

print "-"*60

#2
print "#2"
print "����� ����� ���� ������"
ls2=["wqwq","212nkjmklkl","smkwsk","qwqwsqws"]
print ls2
print dict(zip(ls2,map(lambda x:len(x),ls2)))

print "-"*60

#3
print "#3"
print "�������, ������������ �������, ���������� ����� � �������� �������"
funct=lambda x:x*x*x
n=5
print "��� ����� ",n,"= ",funct(5)

print "-"*60

#4
print "#4"
print "������� � lambda ��������"
funct1=lambda x: x-1
funct2=lambda x: x+1
funct3=lambda x: -x
funct4=lambda x: x*x


d={'dec':funct1,'inc':funct2,'neg':funct3,'sq':funct4}

print "n= ",n
print "��������� ",n,"= ",d['dec'](n)
print "��������� ",n,"= ",d['inc'](n)
print "�������� ",n,"= ",d['neg'](n)
print "������� ",n,"= ",d['sq'](n)




