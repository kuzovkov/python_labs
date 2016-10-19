# encode=utf-8
import re

#глобальные переменные
inputFile = 'Tech1.txt' #имя входного файла
reportFile = 'report.count.words1.txt' #файл со статистикой
MIN_LENGHT = 3 #минимальная длина слова
encode ='' #кодировка файла

cutSpace = re.compile('\s{2,}')

#читаем содержимое файла в строку
def readFile( filename ):
    global encode
    codepage1 = 'utf8'
    codepage2 = 'cp1251'
    try:
        text = open( filename, 'r' ).read().decode( codepage1 )
        encode = codepage1
    except IOError:
        print 'Can not open file ' + filename
        return False
    except UnicodeDecodeError:
        text = open( filename, 'r' ).read().decode( codepage2 )
        encode = codepage2
        return text
    else:
        return text
    
#разбиваем строку на слова
def textSplit( text ):
    words=[]
    cutChars = ['.', ',', '!', '?', '"', '\'', ':', '-', '=', '(', ')', '`', '/', '\\', '*', '&', '%', '$', '#', '>', '<', ';', '[', ']', '{', '}']
    for char in cutChars:
        text = text.replace( char, ' ' )
    text = text.replace( '\n', ' ' )
    text = cutSpace.sub( ' ', text)
    text = text.upper()
    ls_words = text.split()
    for word in ls_words:
        clear_word = clearWord( word )
        if clear_word != None:    
            if len( clear_word ) > MIN_LENGHT:
                words.append( clear_word )
    del ls_words
    return words

#очистка слова от символов которые не буквы
def clearWord( word ):
    outWord=''
    for char in word:
        if char.isalpha():
            outWord+=char
    if len(outWord) != 0:
        return outWord
    else:
        return None

text = readFile( inputFile )
words = textSplit( text )

#подсчет частоты встречаемости слов в списке слов
def countWords( words ):
    countWords={}
    for word in words:
        if countWords.has_key( word ):
            countWords[word] = countWords.get( word ) + 1
        else:
            countWords.update({word:1})
    return countWords


#получаем словарь со статистикой
countWords = countWords( words )
#получае ключи-слова из словаря
words_sort = countWords.keys()
#сортируем слова
words_sort.sort()

#пишем в файл результаты
try:
    fout = open( reportFile, 'w' )
except IOError:
    print 'Can not open file ' + reportFile
else:
    for word in words_sort:
        row = '<' + word.encode( encode ) + '>:<' + str( countWords[word] ) + '>\n'
        fout.write( row )
    fout.close()
    print 'Done'
