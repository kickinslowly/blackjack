import pyautogui
import pydirectinput
import time

token = pyautogui.locateCenterOnScreen('25.png')
betBox = pyautogui.locateCenterOnScreen('bet_box.png')

insurance = pyautogui.locateCenterOnScreen('insurance.png')
deal = pyautogui.locateCenterOnScreen('deal.png')
rebet = pyautogui.locateCenterOnScreen('rebet.png')

three = pyautogui.locateCenterOnScreen('3.png', confidence=.9)
threeThirteen = pyautogui.locateCenterOnScreen('3_13.png', confidence=.9)
nine = pyautogui.locateCenterOnScreen('9.png', confidence=.9)
ten = pyautogui.locateCenterOnScreen('10.png', confidence=.9)
eleven = pyautogui.locateCenterOnScreen('11.png', confidence=.9)
twelve = pyautogui.locateCenterOnScreen('12.png', confidence=.9)
thirteen = pyautogui.locateCenterOnScreen('13.png')
fourteen = pyautogui.locateCenterOnScreen('14.png', confidence=.9)
fifteen = pyautogui.locateCenterOnScreen('15.png', confidence=.9)
sixteen = pyautogui.locateCenterOnScreen('16.png', confidence=.9)
seventeen = pyautogui.locateCenterOnScreen('17.png', confidence=.9)
eighteen = pyautogui.locateCenterOnScreen('18.png')
nineteen = pyautogui.locateCenterOnScreen('19.png', confidence=.9)
twenty = pyautogui.locateCenterOnScreen('20.png', confidence=.9)


def refresh():
    global insurance
    global deal
    global rebet
    global three
    global threeThirteen
    global eight
    global nine
    global ten
    global eleven
    global twelve
    global thirteen
    global fourteen
    global fifteen
    global sixteen
    global seventeen
    global eighteen
    global nineteen
    global twenty

    insurance = pyautogui.locateCenterOnScreen('insurance.png')
    deal = pyautogui.locateCenterOnScreen('deal.png')
    rebet = pyautogui.locateCenterOnScreen('rebet.png')
    three = pyautogui.locateCenterOnScreen('3.png', confidence=.9)
    threeThirteen = pyautogui.locateCenterOnScreen('3_13.png', confidence=.9)
    eight = pyautogui.locateCenterOnScreen('8.png', confidence=.9)
    nine = pyautogui.locateCenterOnScreen('9.png', confidence=.9)
    ten = pyautogui.locateCenterOnScreen('10.png', confidence=.9)
    eleven = pyautogui.locateCenterOnScreen('11.png', confidence=.9)
    twelve = pyautogui.locateCenterOnScreen('12.png', confidence=.9)
    thirteen = pyautogui.locateCenterOnScreen('13.png', confidence=.9)
    fourteen = pyautogui.locateCenterOnScreen('14.png', confidence=.9)
    fifteen = pyautogui.locateCenterOnScreen('15.png', confidence=.9)
    sixteen = pyautogui.locateCenterOnScreen('16.png', confidence=.9)
    seventeen = pyautogui.locateCenterOnScreen('17.png', confidence=.9)
    eighteen = pyautogui.locateCenterOnScreen('18.png', confidence=.9)
    nineteen = pyautogui.locateCenterOnScreen('19.png', confidence=.9)
    twenty = pyautogui.locateCenterOnScreen('20.png', confidence=.9)


def start():
    pyautogui.moveTo(token)
    time.sleep(1)
    pyautogui.dragTo(betBox)
    pyautogui.click()
    time.sleep(1)


def check(x):
    pyautogui.moveTo(x)
    pyautogui.click()


def stand():
    pyautogui.moveTo(1725, 790)
    pyautogui.click()


def hit():
    pyautogui.moveTo(1733, 617)
    pyautogui.click()


time.sleep(2)

poker_count = 0


def poker():
    global poker_count
    while True:
        poker_count += 1
        print(poker_count)
        refresh()
        if insurance:
            check(insurance)
            print('insurance')
            time.sleep(2)
            refresh()
        elif deal:
            check(deal)
            print('deal')
            refresh()
        elif rebet:
            check(rebet)
            print('rebet')
            time.sleep(2)
            refresh()
        if ten or eleven or twelve or thirteen or fourteen or fifteen:
            hit()
            print('Hitting because low')
            time.sleep(2)
            refresh()
            if ten or eleven or twelve or thirteen or fourteen or fifteen:
                hit()
                print('Hitting because low')
                time.sleep(2)
                refresh()
                if ten or eleven or twelve or thirteen or fourteen or fifteen:
                    hit()
                    print('Hitting because low')
                    time.sleep(2)
                    refresh()
        elif sixteen or seventeen or eighteen or nineteen or twenty:
            stand()
            print('Standing')
            time.sleep(2)
            refresh()
        else:
            hit()
            print('Hitting because all else failed')
            time.sleep(2)


start()
poker()
