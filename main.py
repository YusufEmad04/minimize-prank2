import pyautogui
import time
import keyboard
import threading

lock = threading.Lock()
arr = []
s = True


def add_to_arr(i, a):
    lock.acquire()
    if len(a) == 0:
        a.append(i)
    else:
        if i != a[-1]:
            a.append(i)

    if len(a) >= 4:
        a.pop(0)

    print(a)
    lock.release()


def check_for_exit():
    global s
    while True:
        add_to_arr(keyboard.read_key(), arr)
        if len(arr) >= 3:

            # terminates program
            if arr[0] == "e" and arr[1] == "n" and arr[2] == "d":
                lock.acquire()
                s = False
                lock.release()

            # continue
            elif arr[0] == "s" and arr[1] == "r" and arr[2] == "t":
                lock.acquire()
                s = True
                lock.release()


t = threading.Thread(target=check_for_exit)
t.start()

pyautogui.FAILSAFE = True

x = int(pyautogui.size()[0]) - 1
y = int(pyautogui.size()[1]) - 1

while True:
    print(s)
    time.sleep(5)

    if s:
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(int(x / 2), int(y / 2))
        time.sleep(0.15)
        pyautogui.keyDown('esc')
        time.sleep(0.15)
        # pyautogui.click(clicks=2)
        time.sleep(0.15)
        pyautogui.moveTo(x, y)
        time.sleep(0.15)
        pyautogui.click(clicks=2)
