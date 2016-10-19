#разделение полного имени файла на каталог и файл

fullname='C:/dir1/dir2/file.ext'

ls=fullname.split('/')
filename=ls[len(ls)-1]
print filename


path=''
for i in range(len(ls)-1):
    if i < len(ls)-2:
        path+=ls[i]+'/'
    else:
        path+=ls[i]

print path

