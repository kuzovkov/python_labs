#Кузовков Александр Владимирович
import random

def quit():
    print "Для выхода введите q"
    c=raw_input()
    if c=='':
        c='1'
    c=c[0]
    if c =='q':
        return True
    else:
        return False

def main():
    print 'Игра "Угадай число"'
    print 'Правила игры...'
    print 'для досрочного выхода из игры введите 0'
    num_rand=random.randrange(1,25,1)
    num_user=30
    count=0
    while num_user !=0:

        num_user=raw_input('введите число:')
        if num_user=='':
            num_user=0
        num_user=int(num_user)
        count=count+1
        if num_user > num_rand:
            print 'Ваше число больше'
        elif num_user < num_rand:
            print 'Ваше число меньше'
        else:
            print 'Вы угадали число',num_rand,'с',count,'попытки'
            if quit():
                return
            else:
                main()
    
    

main()

    
