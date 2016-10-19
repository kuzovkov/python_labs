#сортировка списка списков
ls1=[
['dfgee1w','hg1fd','wer1ty','er1ty','asd1fg'],
['afgee2w','hg2fd','wer2ty','er2ty','dsd2fg'],
['dfgee3w','ag3fd','wer3ty','ert3y','asdf3g'],
['wfgee4w','hg4fd','cer4ty','art4y','dsd4fg'],
    ]




def printList(ls):
    for row in ls:
        print row
    print "-"*60


def sortList(ls,index):
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
            if minItem > ls[i][index]:
                minItem=ls[i][index]
                tempIndex=i
        indexSorted.append(tempIndex)
    for item in indexSorted:
        lsSorted.append(ls[item])
    return lsSorted





printList(ls1)

printList(sortList(ls1,0))
printList(sortList(ls1,1))
printList(sortList(ls1,2))
printList(sortList(ls1,3))
printList(sortList(ls1,4))


