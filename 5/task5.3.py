#�������� ��������� ������������
import re

filename=raw_input("������ ��� �����: ")
email=re.compile('\w[^\s\n]+@\w{1,}[.][^\s\n]{2,}')
repl=re.compile('[,;\n]')

#filename="text1.txt"
fin=open(filename,"r")

stroka=fin.read()
fin.close()

stroka=repl.sub(' ',stroka)
ls_m=email.findall(stroka)

#print ls_m
print "��������� email � ����� ",filename,":"
for mail in ls_m:
    print mail






