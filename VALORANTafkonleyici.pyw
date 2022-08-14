from os import popen, system
from time import sleep
from pyautogui import position, click, press

fihrist = open("saniye.txt")
uyku = fihrist.read()
print('hata yok')
while True:
    cikti = popen('tasklist').read()
    if("VALORANT.exe" in cikti):#VALORANT.exe
        print("çalışıyor")
        while True:
            position_1 = position()
            print(position_1)
            sleep(int(uyku))
            position_2 = position()
            print(position_2)
            cikti2 = popen('tasklist').read()
            if(not "VALORANT.exe" in cikti2):
                print("kapandı")
                break
            if(position_1 == position_2):
                print("sıkmaya başlandı")
                while True:
                    #click()
                    sleep(1)
                    try:
                        press('f5')
                    except:
                        pass
                    try:
                        press('b')
                    except:
                        pass
                    try:
                        click(x=915, y=659)
                    except:
                        pass
                    try:
                        press('b')
                    except:
                        pass
                    sleep(1)
                    try:
                        press('g')
                    except:
                        pass
                    sleep(1)
                    position_3 = position()
                    position_3 = str(position_3)
                    position_3.replace('Point(','')
                    position_3.replace(')','')
                    position_3.replace(' ','')
                    position_3.replace('x=','')
                    position_3.replace('y=','')
                    position3 = position_3.split(',')
                    if(position3[0] == "Point(x=915" and position3[1] == " y=659)"):
                        print("eşit")
                    elif(position3[0] != "Point(x=915" and position3[1] != " y=659)"):
                        print("sıkma durduruldu")
                        break
    else:
        print("çalışmadı")
        sleep(5)
