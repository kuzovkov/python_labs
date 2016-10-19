#coding=utf-8
from Tkinter import *
import webbrowser
from ConfigParser import *
import urllib
import urllib2
import re
import htql
import time

#глобальные переменные
res_ls=[] #список результатов поиска
index=0 #индекс строки в списке результатов
iniFile="torrents.ini" #файл конфигурации
queryStarted=False #Флаг отправки запроса
testHost='http://ya.ru' #тестовый хост для проверки сети
torrentH=None #кнопки-заголовки таблицы
titleH=None
sizeH=None
dateH=None
sidH=None
licherH=None
proxyH=None
titleWidth=50 #ширина поля названия раздачи
tableHeight=5 #высота строк таблицы
wrapLength=300 #ширина для переноса текста в поле названия раздачи

sortDirect=[]#список направление сортировки для полей таблицы
for i in range(10): sortDirect.append(True)

root = Tk()
root.title('Torrent Search')
#root.resizable(0,True)


def testInternet(host):
    try:
        urllib.urlopen(host)
    except Exception:
        return False
    else:
        return True
    

def sendGetRequest(searchString,torrentOptions,torrentDefault): #отправка GET запроса
    global queryStarted
    if torrentOptions.has_key('plus'):
        sString=urllib.quote_plus(searchString)
    else:
        sString=urllib.quote(searchString)
    host=torrentOptions['host']
    url=torrentOptions['url']
    if torrentOptions.has_key('url2'):
        url2=torrentOptions['url2']
    else:
        url2=''
    url=host+url+sString+url2
    req=urllib2.Request(url)
    if torrentOptions.has_key('cookie'): req.add_header('Cookie',torrentOptions['cookie'])
    if torrentOptions.has_key('user_agent'): req.add_header('User-Agent',torrentOptions['user_agent'])
    if torrentOptions.has_key('accept_language'): req.add_header('Accept-Language',torrentOptions['accept_language'])
    if torrentOptions.has_key('accept_encoding'): req.add_header('Accept-Encoding',torrentOptions['accept_encoding']) 
    if torrentOptions.has_key('proxy'):
        if torrentOptions['proxy'] == 'yes':
            req.set_proxy(torrentDefault['proxy'],'http')
    try:
        res=urllib2.urlopen(req)
    except Exception:
        return False
    else:
        f=open('temp.html','w')
        f.write(res.read())
        f.close()
        f=open('temp.html','r')
        htmlContent=f.read()
        f.close()
        return htmlContent

  
    
def sendPostRequest(searchString,torrentOptions,torrentDefault):#отправка POST запроса
    global queryStarted
    host=torrentOptions['host']
    url=torrentOptions['url']
    url=host+url
    dataDict={}
    dataDict.clear()
    if torrentOptions.has_key('var_search'): dataDict.update({torrentOptions['var_search']:searchString})
    if torrentOptions.has_key('var1'):
        if torrentOptions.has_key('val1'): dataDict.update({torrentOptions['var1']:torrentOptions['val1']})
    if torrentOptions.has_key('var2'):
        if torrentOptions.has_key('val2'): dataDict.update({torrentOptions['var2']:torrentOptions['val2']})
    
    data=urllib.urlencode(dataDict)
    req=urllib2.Request(url)
    if torrentOptions.has_key('cookie'): req.add_header('Cookie',torrentOptions['cookie'])
    if torrentOptions.has_key('user_agent'): req.add_header('User-Agent',torrentOptions['user_agent'])
    if torrentOptions.has_key('accept_language'): req.add_header('Accept-Language',torrentOptions['accept_language'])
    if torrentOptions.has_key('accept_encoding'): req.add_header('Accept-Encoding',torrentOptions['accept_encoding']) 
    if torrentOptions.has_key('proxy'):
        if torrentOptions['proxy'] == 'yes':
            req.set_proxy(torrentDefault['proxy'],'http')
    req.add_data(data)
    filename="temp.html"
    try:
        res=urllib2.urlopen(req)
    except Exception:
        return False
    else:
        f=open(filename,'w')
        f.write(res.read())
        f.close()
        f=open(filename,'r')
        htmlContent=f.read()
        f.close()
        return htmlContent


def htmlParse(content,torrentOptions,torrentDefault):#разбор html контента, названия, ссылки, размера, даты, сидов, личеров
    global res_ls

    #print content
    #print torrentOptions
    
    boundary=torrentOptions.get('boundary',None)
    prefix=torrentOptions.get('prefix','')
    prefix_download=torrentOptions.get('prefix_download',None)
    title_query=torrentOptions.get('title_query',None)
    title_start=torrentOptions.get('title_start',None)
    title_step=torrentOptions.get('title_step',None)
    
    link_query=torrentOptions.get('link_query',None)
    link_start=torrentOptions.get('link_start',None)
    link_step=torrentOptions.get('link_step',None)

    link_query_torrent=torrentOptions.get('link_query_torrent',None)
    link_start_torrent=torrentOptions.get('link_start_torrent',None)
    link_step_torrent=torrentOptions.get('link_step_torrent',None)
    
    size_query=torrentOptions.get('size_query',None)
    size_start=torrentOptions.get('size_start',None)
    size_step=torrentOptions.get('size_step',None)

    date_query=torrentOptions.get('date_query',None)
    date_start=torrentOptions.get('date_start',None)
    date_step=torrentOptions.get('date_step',None)
    
    sid_query=torrentOptions.get('sid_query',None)
    sid_start=torrentOptions.get('sid_start',None)
    sid_step=torrentOptions.get('sid_step',None)
    
    licher_query=torrentOptions.get('licher_query',None)
    licher_start=torrentOptions.get('licher_start',None)
    licher_step=torrentOptions.get('licher_step',None) 

    #дополнительные параметры
    color=torrentOptions.get('color','#cccccc')
    host=torrentOptions.get('host','')
    proxy="No use"
    if torrentOptions.has_key('proxy'):
        if torrentOptions['proxy'] == 'yes':
            proxy=torrentDefault['proxy']
    encode=torrentOptions.get('encode','utf8')

    #парсинг контента
    cutTag=re.compile('<.[^<>]*>')
    cutSpace=re.compile('\s{2,}')
    cutSpace2=re.compile('&nbsp;')
    cutU=re.compile('<u>.[^<>]*</u>')
    cutQuot=re.compile('&quot;')
    cutCod=re.compile('&#\d{1,};')
    
    if (content):
        #отрезаем лишнее
        if boundary != None: content=content[content.find(boundary)::]
    
        #получаем названия
        queryTitle=title_query
        resTitle=htql.HTQL(content,queryTitle)
        titles=[]
        for title in resTitle:
            title=cutTag.sub('',title)
            title=cutSpace.sub('',title)
            title=cutSpace2.sub(' ',title)
            title=cutQuot.sub('"',title)
            title=title.strip()
            titles.append(title)  
        if title_start != None and title_step != None: titles=titles[int(title_start):len(titles):int(title_step)]
        
         #получаем ссылки
        queryLink=link_query
        resLink=htql.HTQL(content,queryLink)
        links=[]
        for link in resLink:
            link=cutTag.sub('',link)
            link=cutSpace.sub('',link)
            links.append(link)
        if link_start != None and link_step != None: links=links[int(link_start):len(links):int(link_step)]

        #получаем ссылки на torrent файл
        linksTorrent=[]
        queryLink=link_query_torrent
        if not queryLink == None:
            resLink=htql.HTQL(content,queryLink)
            for link in resLink:
                link=cutTag.sub('',link)
                link=cutSpace.sub('',link)
                linksTorrent.append(link)
            if link_start_torrent != None and link_step_torrent != None: linksTorrent=linksTorrent[int(link_start_torrent):len(linksTorrent):int(link_step_torrent)]
        else:
            for i in range(len(links)):
                linksTorrent.append(links[i])
                
        #получаем размер
        querySize=size_query
        resSize=htql.HTQL(content,querySize)
        sizes=[]
        for size in resSize:
            size=cutU.sub('',size)
            size=cutTag.sub('',size)
            size=cutSpace.sub('',size)
            size=cutSpace2.sub(' ',size)
            size=cutCod.sub('',size)
            size=size.strip()
            sizes.append(size)
        if size_start != None and size_step != None: sizes=sizes[int(size_start):len(sizes):int(size_step)]   

        #получаем дату
        queryDate=date_query
        resDate=htql.HTQL(content,queryDate)
        dates=[]
        for date in resDate:
            date=cutU.sub('',date)
            date=cutTag.sub('',date)
            date=cutSpace.sub('',date)
            date=cutSpace2.sub(' ',date)
            date=date.strip()
            dates.append(date)
        if date_start != None and date_step != None: dates=dates[int(date_start):len(dates):int(date_step)]
        
        #получаем сидов
        querySid=sid_query
        resSid=htql.HTQL(content,querySid)
        sids=[]
        for sid in resSid:
            sid=cutTag.sub('',sid)
            sid=cutSpace.sub('',sid)
            sid=cutSpace2.sub(' ',sid)
            sid=sid.strip()
            sids.append(sid)
        if sid_start != None and sid_step != None: sids=sids[int(sid_start):len(sids):int(sid_step)]

        #получаем личеров
        queryLicher=licher_query
        resLicher=htql.HTQL(content,queryLicher)
        lichers=[]
        for licher in resLicher:
            licher=cutTag.sub('',licher)
            licher=cutSpace.sub('',licher)
            licher=cutSpace2.sub(' ',licher)
            licher=licher.strip()
            lichers.append(licher)
        if licher_start != None and licher_step != None: lichers=lichers[int(licher_start):len(lichers):int(licher_step)]


        
        #output (for debug)
        '''
        for ls in (titles,links,sizes,dates,sids,lichers):
            print len(ls)
            for item in ls:
                print item
        # end output
        '''
        minLengthItem = min( len(titles),len(links),len(sizes),len(dates),len(sids),len(lichers),len(linksTorrent))
    
        if minLengthItem == 0:
            mess(torrentOptions['name']+' Fail: Nothing found ','Arial 20','#ff0000')
            #res_ls.append([torrentOptions['name'],'Nothing found :-(','-','-',host,proxy,color,encode,'-','-','-',host])
        else:   
            for i in range(minLengthItem):
                if prefix_download == None:
                    res_ls.append([torrentOptions['name'],titles[i],sizes[i],dates[i],host+prefix+links[i],proxy,color,encode,sids[i],lichers[i],host+prefix+linksTorrent[i],host])
                else:
                    res_ls.append([torrentOptions['name'],titles[i],sizes[i],dates[i],host+prefix+links[i],proxy,color,encode,sids[i],lichers[i],prefix_download+linksTorrent[i],host])
            mess(torrentOptions['name']+' Ok','Arial 20','#00ff00')
    else:
        mess(torrentOptions['name']+' Fail: can\'t get content from server ','Arial 20','#ff0000')
        #res_ls.append([torrentOptions['name'],'Can\'t get content from server :-(','-','-',host,proxy,color,encode,'-','-','-',host])


def sendRequestTorrent(searchString,torrentOptions,torrentDefault): 
    global queryStarted
    if not queryStarted: #если запрос уже не отправлен
        if not torrentOptions.has_key('method'): #проверяем тип запроса и отправляем соответсвующий
            return False
        elif torrentOptions['method'] == 'get':
            return sendGetRequest(searchString,torrentOptions,torrentDefault)
        elif torrentOptions['method'] == 'post':
            return sendPostRequest(searchString,torrentOptions,torrentDefault)


def getSearchResult(inifile=iniFile): #получение результата поиска
    global entry
    
    #читаем конфигурационный файл
    conf=ConfigParser()
    conf.read(inifile)
    torrentOptions={}#словарь опций торрента
    torrentDefault={}#словарь опций DEFAULT
    torrentDefault.clear()
    if conf.has_option('DEFAULT','proxy'):  #считываем опции DEFAULT
        torrentDefault.update({'proxy':conf.get('DEFAULT','proxy')})
    for section in conf.sections():  #для каждой секции (каждого торрента) инициализируем переменые для запроса
        torrentOptions.clear()
        for option in conf.options(section):
            torrentOptions.update({option:conf.get(section,option)})
        torrentOptions.update({'name':section})
        searchString=searchEntry.get().encode(torrentOptions.get('encode','utf8')) #читаем строку поиска, преобразуем в нужную кодировку
        #делаем запрос к сайту, получаем контент
        content=sendRequestTorrent(searchString,torrentOptions,torrentDefault)
        #парсим контент, получаем список, добавляем его в res_ls
        htmlParse(content,torrentOptions,torrentDefault)

def mess(message,font='Arial 40',fg='#ff0000'): #выводим сообщение в окно
    global textbox, logText
    messWin=Label(text=message,font=font,width=1200/int(font.split(' ')[1]),bg='#ffffff',fg=fg)
    textbox.window_create(END,window=messWin)
    textbox.update()
    logText.insert(END, message + '\n')
    logText.update()
    time.sleep(1)
    

def sortList(ls,index): #сортировка списка по заданному полю
    global sortDirect
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
            if sortDirect[index]:                
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

def sortBy(index): # сортировка списка с результатами и повторный его вывод в окно
    global res_ls,torrentH,titleH,sizeH,dateH,sidH,licherH,proxyH,sortDirect
    res_ls=sortList(res_ls,index)
   
    if sortDirect[index]:
        sortDirect[index] = False
    else:
        sortDirect[index] = True
    
    printResultList()
    for header in (torrentH,titleH,sizeH,dateH,sidH,licherH,proxyH):
        header.configure(bg="#777777")
    if index == 0: torrentH.configure(bg="#999999")
    if index == 1: titleH.configure(bg="#999999")
    if index == 2: sizeH.configure(bg="#999999")
    if index == 3: dateH.configure(bg="#999999")
    if index == 8: sidH.configure(bg="#999999")
    if index == 9: licherH.configure(bg="#999999")
    if index == 4: proxyH.configure(bg="#999999")

def createHeaders(color="#777777"):
    global textbox,textHeader,torrentH,titleH,sizeH,dateH,sidH,licherH,proxyH,titleWidth
    #размещение заголовков в textbox
    hframe=Frame(width=800,height=20)
    torrentH=Button(hframe,text='Torrent', height=1,width=20,bg=color,justify='center', bd=2, command=lambda index=0: sortBy(index))
    torrentH.pack(side='left')
    titleH=Button(hframe,text='Title', width=titleWidth,height=1,bg=color,justify='center', bd=2,command=lambda index=1: sortBy(index))
    titleH.pack(side='left')
    sizeH=Button(hframe,text='Size', width=7,height=1,bg=color, bd=2,justify='center',command=lambda index=2: sortBy(index))
    sizeH.pack(side='left')
    dateH=Button(hframe,text='Date', width=16,height=1,bg=color, bd=2,justify='center',command=lambda index=3: sortBy(index))
    dateH.pack(side='left')
    sidH=Button(hframe,text='S', width=4,height=1,bg=color, bd=2,justify='center',command=lambda index=8: sortBy(index))
    sidH.pack(side='left')
    licherH=Button(hframe,text='L', width=4,height=1,bg=color, bd=2,justify='center',command=lambda index=9: sortBy(index))
    licherH.pack(side='left')
    proxyH=Button(hframe,text='Proxy', width=22,height=1,bg=color, bd=2,justify='center',command=lambda index=5: sortBy(index))
    proxyH.pack(side='left')
    textHeader.window_create(END,window=hframe)

def printResultList():#вывод результатов поиска из списка в окно
    global textbox,res_ls,index,titleWidth,tableHeight,wrapLength
    index=0
    textbox.delete(1.0,END)
    textbox.update()
    for item in res_ls:        
        frame=Frame(width=800,height=43)
        torrent=Button(frame,text=item[0], height=tableHeight,width=20,bg=item[6],justify='left',command=lambda x=index: goHost(x))
        torrent.pack(side='left')
        title=Button(frame,text=item[1].decode(item[7]), width=titleWidth,height=tableHeight,wraplength=wrapLength,bg=item[6],justify='left',command=lambda x=index: goTopic(x))
        title.pack(side='left')
        size=Button(frame,text=item[2], width=7,height=tableHeight,bg=item[6], bd=2, command=lambda x=index: goDownload(x))
        size.pack(side='left')
        date=Button(frame,text=item[3], width=16,height=tableHeight,bg=item[6], bd=2)
        date.pack(side='left')
        sid=Button(frame,text=item[8], width=4,height=tableHeight,bg=item[6], bd=2)
        sid.pack(side='left')
        licher=Button(frame,text=item[9], width=4,height=tableHeight,bg=item[6], bd=2)
        licher.pack(side='left')
        proxy=Button(frame,text=item[5], width=20,height=tableHeight,bg=item[6], bd=2,justify='center')
        proxy.pack(side='left')
        textbox.window_create(END,window=frame)
        index+=1

def search(e): #при нажатии на кнопку поиска начинаем... 
    global textbox,res_ls,index,queryStarted,testHost
    #начальная инициализация, очистка окна, размещение заголовков 
    if queryStarted:
        return
    textbox.delete(1.0,END)
    textbox.update()
    mess('Please wait...')# выводим please wait
    searchBtn.configure(state='disabled')#гасим кнопку
    searchBtn.update()
    res_ls=[]

    #получение результатов поиска
    if testInternet(testHost):
        getSearchResult()
        textbox.delete(1.0,END)
        textbox.update()
        printResultList()#выводим список результатов в окно
    else:
        mess('Please check you Internet connection!')
    
    searchBtn.configure(state='normal')# включаем кнопку
    queryStarted=False

def Quit(ev):  # выход из приложения
    root.destroy()

def goTopic(i): #переход по ссылке на страницу раздачи
    global res_ls
    webbrowser.open(res_ls[i][4])

def goHost(i): #переход по ссылке на главную торрент-трекера
    global res_ls
    webbrowser.open(res_ls[i][11])

def goDownload(i): #переход по ссылке на торрент-файл
    global res_ls
    webbrowser.open(res_ls[i][10])



# размещение виждетов на главном окне
panelFrame = Frame(root, height = 60, bg = 'gray')
headerFrame = Frame(root, height = 20, width = 600,bg = 'gray')
textFrame = Frame(root, height = 150, width = 600)
logFrame = Frame(root,height = 20, width = 600)

panelFrame.pack(side = 'top', fill = 'x')
headerFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'top', fill = 'both', expand = 1)
logFrame.pack(side = 'bottom', fill = 'both', expand = 1)

logText = Text(logFrame, height = 4, width = 170, font = 'Arial 12' )
scrollbarLog = Scrollbar(logText)

scrollbarLog['command'] = logText.yview
logText['yscrollcommand'] = scrollbarLog.set

textHeader=Text(headerFrame,font='Arial 14',wrap='word',width=50,height=1, bg='gray')
textbox = Text(textFrame, font='Arial 14',width=76, height=20)
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textHeader.pack(side = 'left', fill = 'both', expand = 1)
textbox.pack(side = 'left', fill = 'both', expand=1)
scrollbar.pack(side = 'right', fill = 'y')

logText.pack(side = 'left', fill = 'both', expand = 1)
scrollbarLog.pack(side='right', fill='y')

searchEntry=Entry(panelFrame,width=80,font='arial 12',bd=2)
searchEntry.place(x=10,y=10)
searchBtn = Button(panelFrame, text = 'Search',bd=2)
quitBtn = Button(panelFrame, text = 'Quit',bd=2)

searchBtn.bind("<Button-1>",search)
quitBtn.bind("<Button-1>", Quit)
root.bind("<Return>",search)

searchBtn.place(x = 750, y = 10, width = 40, height = 40)
quitBtn.place(x = 800, y = 10, width = 40, height = 40)

createHeaders()
searchEntry.focus_set()

root.mainloop()
