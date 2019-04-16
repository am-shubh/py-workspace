import pyautogui, time
time.sleep(7)
    # click to put drawing program in focus
distance = 30

def up():
    pyautogui.dragRel(0, -distance, duration=0.2)

def down():
    pyautogui.dragRel(0, distance, duration=0.2)

def left():
    pyautogui.dragRel(-distance,0, duration=0.2)

def right():
    pyautogui.dragRel(distance,0, duration=0.2)

while(distance > 0):
    pyautogui.mouseDown()
    up()
    right()
    down()
    right()
    down()
    left()
    down()
    left()
    up()
    left()
    up()
    right()
    pyautogui.mouseUp()
    pyautogui.dragRel(5,0, duration=0.2)
    distance = distance - 5


