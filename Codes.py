import pyautogui
import time

print("For numbers that go over 100 such at CODE146 through 188(example) just put CODE1 for keyword")
keyword = input("Keyword: ")
firstNumber = int(input("Starting number: "))
secondNumber = int(input("Ending number: "))
frontOrBack = input("Numbers in back or front Ex. 55KEYWORD or KEYWORD55 (f/b): ")
print(" ")
secondNumber+=1
cooldown = time.time()

total_Reedeemed = 0
couldnt_reedeem = 0

#Seconds
wait = 7
def backSpace():
    pyautogui.click(1622, 446)
    pyautogui.click(1622, 446)
    pyautogui.click(1622, 446)
    pyautogui.press('backspace')
    

loops = firstNumber
while loops != secondNumber:
    if frontOrBack.lower() == "b":
        code = str(keyword) + str(loops)
    elif frontOrBack.lower() == "f":
        code = str(loops) + str(keyword)
    if not pyautogui.pixelMatchesColor(1437, 318, (255, 226, 36)):
        #Shop
        time.sleep(0.15)
        pyautogui.click(1870, 831)
        time.sleep(0.15)
        #Code(s)
        pyautogui.click(1030, 715)
        time.sleep(0.15)
    #Click Prize box
    pyautogui.click(1622, 446)
    time.sleep(0.45)
    #Make sure there's nothing in box
    if pyautogui.pixelMatchesColor(1455, 449, (137, 137, 137)):
        backSpace()
    else:
        pass

    pyautogui.write(code)

    if loops == firstNumber:
        pyautogui.click(1445, 523)
        time.sleep(0.15)
        if pyautogui.locateCenterOnScreen('images/expired.png', confidence=0.70, region=(1479, 212, 1587, 258)):
            backSpace()
            print("Failed to Reedeemed #" + str(loops))
        elif pyautogui.pixelMatchesColor(1707, 238, (8, 8, 8)):
            backSpace()
            print("Failed to Reedeemed #" + str(loops))
            
        else:
            total_Reedeemed+=1
            print("Total Reedeemed,", total_Reedeemed)

            time.sleep(0.2)
            
            drop = pyautogui.locateCenterOnScreen('images/skills/continue.png', confidence = 0.90, region = (1340,635,200,65))
            if(drop):
                pyautogui.click(drop)
                
        loops+=1
        
    elif time.time() - cooldown > wait:
        pyautogui.click(1445, 523)
        time.sleep(0.15)
        if pyautogui.locateCenterOnScreen('images/expired.png', confidence=0.70, region=(1479, 212, 1587, 258)):
            #Chat box/Getting everything highlighted
            backSpace()
            print("Failed to Reedeemed #" + str(loops))

        elif pyautogui.pixelMatchesColor(1707, 238, (8, 8, 8)):
            backSpace()
            print("Failed to Reedeemed #" + str(loops))
            
        else:
            total_Reedeemed+=1
            print("\nTotal Reedemed,", total_Reedeemed)

            time.sleep(0.2)
            
            drop = pyautogui.locateCenterOnScreen('images/skills/continue.png', confidence = 0.90, region = (1340,635,200,65))
            if(drop):
                pyautogui.click(drop)
        loops+=1
        cooldown = time.time()
        
    elif time.time() - cooldown < wait:
        print("\n\tWaiting...\n")
        time.sleep(wait - (time.time() - cooldown))
        pyautogui.click(1445, 523)
        time.sleep(0.15)
        if pyautogui.locateCenterOnScreen('images/expired.png', confidence=0.70, region=(1479, 212, 1587, 258)):
            backSpace()
            print("Failed to Reedeemed #" + str(loops))

        elif pyautogui.pixelMatchesColor(1707, 238, (8, 8, 8)):
            backSpace()
            print("Failed to Reedeemed #" + str(loops))
            
        else:
            total_Reedeemed+=1
            print("Reedeemed #" + str(loops))
            print("Total Reedeemed,", total_Reedeemed)

            time.sleep(0.2)
            
            drop = pyautogui.locateCenterOnScreen('images/skills/continue.png', confidence = 0.90, region = (1340,635,200,65))
            if(drop):
                pyautogui.click(drop)
        loops+=1
        cooldown = time.time()
else:
    print("Finished quota of", secondNumber - firstNumber, "Codes.", total_Reedeemed, "Total redeemed.")
        

    
        
    
