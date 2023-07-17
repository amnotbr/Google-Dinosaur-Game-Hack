import cv2
import numpy
import pyautogui
from time import time
import keyboard
import mss
from PIL import Image, ImageGrab
import win32gui, win32ui, win32api, win32con

def get_screenshot():
    hwnd = win32gui.GetDesktopWindow()
    hwnd_dc = win32gui.GetWindowDC(hwnd)
    mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
    save_dc = mfc_dc.CreateCompatibleDC()
    
    x, y, width, height = 654,164,195,136
    
    
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(mfc_dc, width, height)
    save_dc.SelectObject(screenshot)
    
    save_dc.BitBlt((0, 0), (width, height), mfc_dc, (x, y), win32con.SRCCOPY)
    
    # Convert the bitmap to a numpy array
    bmp_info = screenshot.GetInfo()
    bmp_str = screenshot.GetBitmapBits(True)
    img = numpy.frombuffer(bmp_str, dtype=numpy.uint8)
    img = img.reshape((bmp_info['bmHeight'], bmp_info['bmWidth'], 4))
    
    # Clean up resources
    win32gui.DeleteObject(screenshot.GetHandle())
    save_dc.DeleteDC()
    mfc_dc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwnd_dc)
    
    return img


def main():
    loop_time = time()
    
    # loading the images for detection
    dinosaur = cv2.imread("dinosaur.png")
    single_large_cacti = cv2.imread("singlelargecacti.PNG")
    smallcactus = cv2.imread("smallcactus.PNG")
    threecactus = cv2.imread("threecactus.PNG")
    double = cv2.imread("doublecactus.PNG")
    four = cv2.imread("fourcactus.PNG")
    birddown = cv2.imread("birddown.PNG")
    birdup = cv2.imread("birdup.PNG")  
    double_large = cv2.imread("doublelarge.PNG")                                                   
    
    # main loop
    while True:
        screenshot = get_screenshot()
        
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)  # Convert from BGRA to BGR
        screenshot = screenshot.astype(numpy.uint8)  # Convert to uint8 type
        
        # photo detection 

        threshold = 0.8
        dthreshold = .8

        # DINO SAUR
        
        dheight = dinosaur.shape[0]
        dwidth = dinosaur.shape[1]
        #channels = dinosaur.shape[2]
        dres = cv2.matchTemplate(screenshot, dinosaur, cv2.TM_CCOEFF_NORMED)
        
        dloc = numpy.where(dres >= dthreshold)
        for dpt in zip(*dloc[::-1]):  # Switch columns and rows
            end_point = (dpt[0] + dwidth, dpt[1] + dheight)
            cv2.rectangle(screenshot, dpt, end_point, (0, 0, 0), 2)
            #print("Dinosaur")


        # LARGE CACTUS
        
        height = single_large_cacti.shape[0]
        width = single_large_cacti.shape[1]
        channels = single_large_cacti.shape[2]
        res = cv2.matchTemplate(screenshot, single_large_cacti, cv2.TM_CCOEFF_NORMED)
        
        loc = numpy.where(res >= threshold)
        for pt in zip(*loc[::-1]):  # Switch columns and rows
            cv2.rectangle(screenshot, pt, (pt[0] + width, pt[1] + height), (0, 255, 0), 2)
            keyboard.press('space')

            #print("One large Cactus")
            
            
            
        # SMALL CACTUS
        
        height = smallcactus.shape[0]
        width = smallcactus.shape[1]
        channels = smallcactus.shape[2]
        res = cv2.matchTemplate(screenshot, smallcactus, cv2.TM_CCOEFF_NORMED)
        
        loc = numpy.where(res >= threshold)
        for pt in zip(*loc[::-1]):  # Switch columns and rows
            cv2.rectangle(screenshot, pt, (pt[0] + width, pt[1] + height), (0, 255, 0), 2)
            keyboard.press('space')
            #print("small cactus")
            
            
        # THREE CACTUS
        
        height = threecactus.shape[0]
        width = threecactus.shape[1]
        res = cv2.matchTemplate(screenshot, threecactus, cv2.TM_CCOEFF_NORMED)
        three_threshold = 0.7
        loc = numpy.where(res >= three_threshold)
        for pt in zip(*loc[::-1]):  # Switch columns and rows
            cv2.rectangle(screenshot, pt, (pt[0] + width, pt[1] + height), (0, 255, 0), 2)
            keyboard.press('space')   
            #print("three cactus")
            

        # DOUBLECACTUS
        
        height = double.shape[0]
        width = double.shape[1]
        res = cv2.matchTemplate(screenshot, double, cv2.TM_CCOEFF_NORMED)
        
        loc = numpy.where(res >= threshold)
        for pt in zip(*loc[::-1]):  # Switch columns and rows
            cv2.rectangle(screenshot, pt, (pt[0] + width, pt[1] + height), (0, 255, 0), 2)                                                                                                                                                                              
            keyboard.press('space')   
            #print("two cactus")
            
        # FOUR CACTUS CACTUS
        
        height = four.shape[0]
        width = four.shape[1]
        channels = four.shape[2]
        res = cv2.matchTemplate(screenshot, four, cv2.TM_CCOEFF_NORMED)
        
        loc = numpy.where(res >= threshold)
        for pt in zip(*loc[::-1]):  # Switch columns and rows
            cv2.rectangle(screenshot, pt, (pt[0] + width, pt[1] + height), (0, 255, 0), 2)
            keyboard.press('space')   
            #print("four cactus")
            

        # BIRD WINGS DOWN
        
        height = birddown.shape[0]
        width = birddown.shape[1]
        res = cv2.matchTemplate(screenshot, birddown, cv2.TM_CCOEFF_NORMED)
        
        loc = numpy.where(res >= threshold)
        for pt in zip(*loc[::-1]):  # Switch columns and rows
            cv2.rectangle(screenshot, pt, (pt[0] + width, pt[1] + height), (0, 255, 0), 2)
            keyboard.press('space')  
            #print("bird down")
            
        # BIRD WINGS UP
        
        height = birdup.shape[0]
        width = birdup.shape[1]
        res = cv2.matchTemplate(screenshot, birdup, cv2.TM_CCOEFF_NORMED)
        loc = numpy.where(res >= threshold)
        for pt in zip(*loc[::-1]):  # Switch columns and rows
            cv2.rectangle(screenshot, pt, (pt[0] + width, pt[1] + height), (0, 255, 0), 2)
            keyboard.press('space')  

        # double large cactus
    
        height = double_large.shape[0]
        width = double_large.shape[1]
        res = cv2.matchTemplate(screenshot, double_large, cv2.TM_CCOEFF_NORMED)
        loc = numpy.where(res >= threshold)
        for pt in zip(*loc[::-1]):  # Switch columns and rows
            cv2.rectangle(screenshot, pt, (pt[0] + width, pt[1] + height), (0, 255, 0), 2)
            keyboard.press('space')  

        cv2.imshow("Image", screenshot)
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    
if __name__ == "__main__":
    main()