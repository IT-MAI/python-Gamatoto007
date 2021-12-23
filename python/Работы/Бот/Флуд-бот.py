import pyautogui, time
time.sleep(3)
for i in range(1):
    pyautogui.write("Hello World!", interval=0.03)
    pyautogui.press("enter")
