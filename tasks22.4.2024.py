from random import randint

def task1():
    FIO = list(input('Ваше ФИО:  ').split())
    if len(FIO) >= 3:
        print(FIO[0], FIO[1][0] + '.', FIO[2][0] + '.')
    elif len(FIO) == 2:
        print(FIO[0], FIO[1][0] + '.')


def task2(n):
    pass


def task3():
    for iterB in range(10):
        kolvo_deneg1 = 100
        kolvo_deneg1 -= iterB * 10
        for iterK in range(20):
            kolvo_deneg2 = kolvo_deneg1
            kolvo_deneg2 -= iterK * 5
            for iter10T in range(20):
                kolvo_deneg3 = kolvo_deneg2
                kolvo_deneg3 -= iter10T * 5
                if (iter10T * 10 + iterK + iterB == 100) and (kolvo_deneg3 == 0):
                    print(f'быков: {iterB}, коров: {iterK}, телят: {iter10T * 10}')


def task4():
    dostoint = randint(6, 14)
    if dostoint < 11:
        pass
    elif dostoint == 11:
        dostoint = 'валет'
    elif dostoint == 12:
        dostoint = 'дама'
    elif dostoint == 13:
        dostoint = 'король'
    elif dostoint == 14:
        dostoint = 'туз'
    print(dostoint)


def task5(arr_of_marks):
    count2 = arr_of_marks.count(2)
    count3 = arr_of_marks.count(3)
    count4 = arr_of_marks.count(4)
    count5 = arr_of_marks.count(5)
    print('количество 2:', count2)
    print('количество 3:', count3)
    print('количество 4:', count4)
    print('количество 5:', count5)


def task8(vozrast_v_mesyacah):
    kol_vo_let = vozrast_v_mesyacah // 12
    kol_vo_mesyacev = vozrast_v_mesyacah % 12
    if 10 < kol_vo_let % 100 < 20:
        kol_vo_let = str(kol_vo_let) + ' лет'
    elif kol_vo_let % 10 == 1:
        kol_vo_let = str(kol_vo_let) + ' год'
    elif 1 < kol_vo_let % 10 < 5:
        kol_vo_let = str(kol_vo_let) + ' года'
    else:
        kol_vo_let = str(kol_vo_let) + ' лет'
    if kol_vo_mesyacev == 0:
        kol_vo_mesyacev = 'ровно'
    elif kol_vo_mesyacev == 1:
        kol_vo_mesyacev = str(kol_vo_mesyacev) + ' месяц'
    elif kol_vo_mesyacev < 5:
        kol_vo_mesyacev = str(kol_vo_mesyacev) + ' месяца'
    else:
        kol_vo_mesyacev = str(kol_vo_mesyacev) + ' месяцев'
    print(kol_vo_let, kol_vo_mesyacev)


def task9():
    URL_input = input('введите свой URL:  ')
    if URL_input.count('@') >= 1:
        URL = URL_input[URL_input.rfind('@'):]
    else:
        URL = URL_input
    protocol = URL.find('://')
    protocol = URL[0:protocol]
    URL = URL[len(protocol) + 3:]
    host = URL.find('/')
    host = URL[0:host]
    URL = URL[len(host)+1:]
    if URL.count('?') == 1:
        EndPoint = URL.find('?')
        EndPoint = URL[0:EndPoint]
        URL = URL[len(EndPoint)+1:]
    else:
        EndPoint = URL
        URL = ''
    args = []
    if URL.count('&') >= 1:
        args = URL.split('&')
        URL = ''
    else:
        args = URL
        URL = ''
    print(protocol, host, EndPoint, * args, URL)


# http://alpha90/map?x=60&y=90&name=Vasy
