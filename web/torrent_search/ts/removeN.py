#����� �������� �������� �������� ����� �� �����
filename='temp.html'
filenameOut='tempout.html'

f=open(filename,'r')
content=f.read()
f.close

#�������� � ���������
content=content.replace('\n','')
content=content.replace('\t','')
content=content.replace('\v','')

f=open(filenameOut,'w')
f.write(content)
f.close


