# encode=utf-8
import re

#глобальные переменные
inputFile = 'test.txt' #имя входного файла
reportFile = 'report.count.words2.txt' #файл с исключаемыми словами
suffixFile = 'suffix.txt' #Файл с суффиксами
MIN_LENGHT = 3 #минимальная длина слова
encode ='' #кодировка файла
wordTable = []

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
def textSplit( text, minLenght =  MIN_LENGHT ):
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
            if len( clear_word ) > minLenght:
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

#сравнение двух слов
def wordsComp( word1, word2 ):
    word1 = word1.upper()
    word2 = word2.upper()
    rootword = ''
    if ( len( word1 ) - len( word2 ) ) > 2:
        return False
    if len( word1 ) < len( word2 ):
        temp = word1
        word1 = word2
        word2 = temp
    for i in range( len( word2 ) ):
        if word1[i] == word2[i]:
            rootword += word1[i]
    if ( isRoot( word1, rootword )  and isRoot( word2, rootword ) ):
        return True
    else:
        return False
    

#является ли слово от этого корня
def isRoot( word, root ):
    global suffixs
    word = word.upper()
    root = root.upper()
    for suffix in suffixs:
        if root + suffix == word:
            return True
    return False



def sortList(ls,index): #сортировка списка по заданному полю
    sortDirect = True
    indexSorted=[]
    lsSorted=[]
    lsLen=len(ls)
    while len(indexSorted) != lsLen:
        minItem=None
        tempIndex=None
        for i in range(lsLen):
            if i in indexSorted: continue
            if minItem == None:
                minItem=ls[i][index]
                tempIndex=i
            if sortDirect:                
                if minItem > ls[i][index]:
                    minItem=ls[i][index]
                    tempIndex=i
            else:
                if minItem < ls[i][index]:
                    minItem=ls[i][index]
                    tempIndex=i
        indexSorted.append(tempIndex)
    for item in indexSorted:
        lsSorted.append(ls[item])
    return lsSorted

#читаем суффиксы
suffixs = textSplit( readFile( suffixFile ), 0 )
suffixs.append('')
#читаем файл в строку
text = readFile( inputFile )
#получаем список слов
words = textSplit( text )

#набираем статистику
countWords = len( words )
for k in range( countWords ):
    if len( wordTable ) == 0:
        wordTable.append( [words[k]] )
        continue
    flag_new_word = True
    for i in range( len( wordTable ) ):
        if wordsComp( wordTable[i][0], words[k] ):
            wordTable[i].append( words[k] )
            flag_new_word = False
            break
    if ( flag_new_word ):
        wordTable.append( [words[k]] )
        #print len( wordTable )
        proc = float(k*100)/countWords
        print '%2.2f procentes done' % proc 

#сортируем результат
wordTable = sortList( wordTable, 0 )

#записываем в файл
try:
    fout = open( reportFile, 'w' )
except IOError:
    print 'Can not open file ' + reportFile
else:
    for record in wordTable:
        row = '<'
        num = len( record )
        record = list( set( record ) )
        for i in range( len( record ) ):
            row += record[i].encode( encode )
            if i < ( len( record ) - 1 ):
                row += ','
        row += '>:<' + str( num ) + '>\n'
        fout.write( row )
    fout.close()
    print 'Done'

