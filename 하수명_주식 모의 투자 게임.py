import random
import time

# 주가 dict 묶음, key 리스트
Smoney1 = {'대한항공' : 28850, '현대차' : 183500 , '하이닉스': 104000, '삼성전자':65500, '카카오':81900, '셀트리온': 159000}
sl = list(Smoney1.keys())
# player 들 돈 dict 묶음
Pmoney = {'YOU':10000000, 'CPU1' : 10000000 , 'CPU2': 10000000, 'CPU3':10000000, 'CPU4':10000000, 'CPU5': 10000000}
# player 의 주식 리스트
stock_list1=[]
# 주가, 잔고 변동
r1=[0,0,0,0,0,0]
r2=list(range(-15,15))
round = 1   #라운드 = 10까지

# 꾸미기용 함수 정의
def printbar():
    print('----------------------------------------------------------------')
def sleep():
    time.sleep(0.5)
def skip():
    for i in range(3):
        print('$')
        sleep()

# 기능용 함수 정의
def buy(num):
    if num not in [1, 2, 3, 4, 5, 6]: #  이외의 것은 없는 주식으로 다시 되돌아 가게 한다
        sleep()
        print('잘못 입력 하였습니다.')
        sleep()
        printbar()
    else :
        print(f'최대  {Pmoney["YOU"] // Smoney1[sl[num-1]]}개') #살수 있는 개수 표기
        count = int(input('매수 수량을 입력해 주세요  :')) # 매수 수량 입력 받기
        if Pmoney['YOU']-Smoney1[sl[num-1]]*count<0: #보유금액 - 주가 * 갯수 가 0보다 작을때
            print('돈이 부족합니다.')
            sleep()
            printbar()
        else:
            Pmoney['YOU']= Pmoney['YOU'] - Smoney1[sl[num-1]] * count #보유금액 - 주가 * 갯수 가 0보다 클때
            for i in range(count):
                stock_list1.append(sl[num-1]) #count 만큼 주식을 주식리스트에 추가한다
            print('거래 완료')
            sleep()
            printbar()

def sell(num):
    if num not in [1, 2, 3, 4, 5, 6]: #  이외의 것은 없는 주식으로 다시 되돌아 가게 한다.
        sleep()
        print('잘못 입력 하였습니다.')
        sleep()
        printbar()
    else :
        print(f'보유 갯수  :  {stock_list1.count(sl[num-1])}') #현재 매도수 있는 갯수를 표기
        sellcount = int(input('매도 수량을 입력해 주세요  : ')) #매도 갯수를 입력 받는다

        if stock_list1.count(sl[num-1])-sellcount<0: #보유개수-매도개수 가 0보다 작을때
            print('error')
            sleep()
            printbar()

        else:
            Pmoney['YOU']= Pmoney['YOU'] + Smoney1[sl[num-1]] * sellcount
            #보유 금액에 현재 주가 * 매도 개수를 추가한다
            for i in range(sellcount):# sellcount 만큼 반복
                stock_list1.remove(sl[num-1])#주식리스트에서 제거

            print('거래 완료')
            sleep()
            printbar()

enter = input('press to start  ')

while round !=11:
    sleep()
    printbar()
    print(f"{round}회차 입니다.\t\t 보유금액 : {Pmoney['YOU']}원")#회차 및 보유금액 정보

    for num in [0,1,2,3,4,5]:# 현재 주가와 등락률을 보여준다
        print(f"{num+1}.{sl[num]}\t\t{Smoney1[sl[num]]}원" , end='')
        if int(r1[num]) > 0 :
            print('\033[41m'+'\033[30m'+str(r1[num])+'%'+'\033[0m')
        else :
            print('\033[44m'+'\033[30m'+str(r1[num])+'%'+'\033[0m')

    menu = input('[1 : 매수  2 : 매도  3 : 현황  4 : 턴넘기기 ]  :') #메뉴 입력 받기

    if menu == '1': #메뉴 입력값이 1일때 buy 함수 사용
        sleep()
        printbar()
        number = int(input('종목을 정해 주세요  : '))
        buy(number)

    elif menu == '2':#메뉴 입력값이 2일때 sell 함수 사용
        printbar()
        sleep()
        number = int(input('종목을 정해 주세요  : '))
        sell(number)

    elif menu == '3':#메뉴 입력값이 3일때
        sleep()
        printbar()
        print('주식보유현황 \n')

        for stock in Smoney1.keys():# 주식 리스트에 보유갯수 카운트
            print(f'{stock} :   {stock_list1.count(stock)}')

        sleep()
        print('다른플레이어 보유금액')# 다른 플레이어 보유금액 표기
        print('CPU1', Pmoney['CPU1'], 'CPU2', Pmoney['CPU2'], 'CPU3', Pmoney['CPU3'], 'CPU4', Pmoney['CPU5'], 'CPU5', Pmoney['CPU5'])
        sleep()

    elif menu == '4':#메뉴 입력값이 4일때
        skip()
        print('턴을 넘깁니다')

        if round != 10: #라운드가 10 이 아니면
            r1 = [random.randint(-30, 30) for value in range(6)] #6개의 -30과 30 사이의 랜던 값 6개를 리스트로 받는다
            for player in ('CPU1','CPU2','CPU3','CPU4','CPU5'): #랜덤으로 등락율 결정
                    Pmoney[player] = Pmoney[player] + Pmoney[player] * random.choice(r2) // 100
            for num in [0,1,2,3,4,5]: #랜덤으로 등락율 결정
                Smoney1[sl[num]] = Smoney1[sl[num]] + Smoney1[sl[num]] * r1[num] // 100
            round += 1     # 라운드가 늘어난다
        else :
            break

    else : #메뉴 입력 값이 1,2,3,4,가 아닌경우
        print('잘못 입력 하셨습니다.')
        printbar()
        sleep()

printbar()
skip()
print('결과를 출력합니다. 보유한 주식을 처분합니다.')

while len(stock_list1) !=0: #주식리스트의 요소 수가 0이 될때 까지

        for stock in sl:
            if stock in stock_list1: # 주식리스트에서 제거 및 보유 금액 증가
                stock_list1.remove(stock)
                Pmoney['YOU'] = Pmoney['YOU'] + Smoney1[stock]

for player in Pmoney.keys(): # player 별 보유 금액 프린트
    sleep()
    print(f"{player}\t:\t{Pmoney[player]}원")

printbar()
print('순위')

rank = sorted(Pmoney,reverse=True , key=Pmoney.get)# dict 를 내림 차순으로 key만 추출
for num in range(6): #순위 표기
    sleep()
    print(f"{num+1}위 : {rank[num]}")

