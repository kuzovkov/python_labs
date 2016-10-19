import re

#���������� ����������
templateFiles = 'templates.txt' #���� �� ������� ������ ��������
inputFile = 'input.file.txt' #���� � ������ �������� �����
excWordsFile = 'cut_words.txt' #���� � ������������ �������
suffixFile = 'suffix.txt' #���� � ����������


cutSpace = re.compile('\s{2,}')


#������ ������ ������ �������� �� ����� ������������
def readListTemplates( filename ):
    try:
        ls_files = open( filename, 'r' ).read().split('\n')
    except IOError:
        print 'Can not open file ' + filename
        return False 
    else:
        return ls_files

#������ ���������� �������� �����
def readInputFile( filename ):
    try:
        inputText = open( (open( inputFile , 'r' ).read() ).strip(), 'r').read()
    except IOError:
        print 'Can not open file ' + inputFile
        return False
    else:
        return inputText


#������ ���������� ����� � ������
def readFile( filename ):
    try:
        text = open( filename, 'r' ).read()
    except IOError:
        print 'Can not open file ' + filename
        return False
    else:
        return text
    
#��������� ���� �� �����
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
        words.append( clearWord( word ) )
    del ls_words
    return words

#������� ����� �� �������� ������� �� �����
def clearWord( word ):
    outWord=''
    for char in word:
        if char.isalpha():
            outWord+=char
    if len(outWord) != 0:
        return outWord
    else:
        return None

#������ ������ ����, ����������� �������� �� �����
def readListWords( filename ):
    try:
        text = open(filename, 'r' ).read()
    except IOError:
        print 'Can not open file ' + filename
    else:
        text = text.replace( '\n', '' )
        text = text.replace( ' ', '' )
        text = text.upper()
        return text.split(',')

#��������� ���� ����
def wordsComp( word1, word2 ):
    word1 = word1.upper()
    word2 = word2.upper()
    if len( word1 ) < len( word2 ):
        temp = word1
        word1 = word2
        word2 = temp
    count = 0
    for i in range( len( word2 ) ):
        if word1[i] == word2[i]:
            count+=1
    return float(count)/len( word2 )


ls_files = readListTemplates( templateFiles )
text = readInputFile( 'Tech1.txt' )

print '-'*60

'''
for f in ls_files:
    print readFile( f )
    print '-'*60
'''
for word in textSplit( text ):
    print word

for word in readListWords( suffixFile ):
    print word 


print wordsComp('��������','��������')
