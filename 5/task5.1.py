# �������� ��������� ������������
# ������������ ������ � �����

file_in=raw_input("������� ��� ��������� �����: ")


file_out="out_"+file_in

#��������� ������ ������
width=50

try:
    fin=open(file_in,"r")
except IOError:
    print "�� ���� ������� ����",file_in
else:
 

    
    try:
        fout=open(file_out,"w")
    except IOError:
        print "�� ���� ������� ����",file_out
    else:
        
        #������ �� ����� � ������ �����
        stringstmp=fin.readlines()
        fin.close()

        
    #�������� ������� ����� �� �����
        strings=[]
        for strtmp in stringstmp:
            k=int(len(strtmp)/width)
            if k!=0:
                for i in range(k+1):
                    strings.append(strtmp[i*width:(i+1)*width].rstrip("\n")+"\n")
                    
            else:
                strings.append(strtmp)
                
            
         #��������� ����� ����� ���������� �������� �������   
        for stroka in strings:
            spase=width-len(stroka)
            if spase%2==0:
                left_spase=int(spase/2)
            else:
                left_spase=int(spase/2)+1
            stroka=" "*left_spase+stroka
            fout.write(stroka)
        fout.close()

        print "��������� (��. ���� ",file_out,")"


        #print open.__doc__
        #print file.__doc__
