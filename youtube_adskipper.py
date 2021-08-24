import cv2
import numpy as np
import pyautogui
import time
 
# lendo os templates
template1 = cv2.imread('template3.png', 0)
template2 = cv2.imread('template4.png', 0)
template3 = cv2.imread('template5.png', 0)
template4 = cv2.imread('template6.png', 0)
template5 = cv2.imread('template6.png', 0)
 
threshold = 0.7
 
pyautogui.alert(text = 'Mantenha o cursor no canto superior esquerdo para interromper o programa', title= 'Critério de Interrupção')

def checking (template):
    res = cv2.matchTemplate(im1, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    return loc

def clicking (loc):
    if loc[0].size != 0:
        pyautogui.click(list(zip(*loc[::-1]))[0])
        continue
    else:
        pass
    
while True:
    time.sleep(1)
    im1 = pyautogui.screenshot()
    im1 = np.asarray(im1.convert(mode = 'L'))

    loc1 = checking (template1)
    clicking (loc1)
    
    loc2 = checking (template2)
    clicking (loc2)
    
    loc3 = checking (template3)
    clicking (loc3)
        
    loc4 = checking (template4)
    clicking (loc4)
    
    loc5 = checking (template5)
    clicking (loc5)
    
    if pyautogui.position() == (0,0):
        pyautogui.alert(text = 'Ads Skipper foi fechado', title = 'Adskipper Closed')
        break
