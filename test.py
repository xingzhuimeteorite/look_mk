import pyautogui 
import time 

print('键鼠监听') 

screenWidth, screenHeight =  pyautogui.size() 

print(screenWidth,screenHeight)  

currentMouseX, currentMouseY = pyautogui.position()  

print(currentMouseX, currentMouseY) 



pyautogui.move(0, 10) 

while(1):
    print(pyautogui.position()) 
    time.sleep(2)
    pyautogui.move(0, 100)       