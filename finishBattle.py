import pyautogui as MI
import time
import math

MI.PAUSE = 0.001

def finish(kills, losses):
    victory = False
    if(MI.locateCenterOnScreen('images/victoryX.png',confidence = 0.85, region = (1172, 417, 137, 272))):
        kills = kills + 1
        victory = True
        print("\tBattle Result: Win\n")
        
    elif(MI.locateCenterOnScreen('images/defeatX.png',confidence = 0.85, region = (1193, 453, 120, 155))):
        losses = losses + 1
        victory = False
        print("\tBattle Result: Loss\n")

    #print("X Button found:")
    #Did you know yellow
    #if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
        #pass
    #else:
        # x1)
        #return kills, losses, victory
    
    for i in range(1):
        x = MI.locateCenterOnScreen('images/xButton/xbutton1.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 1")
            
        time.sleep(0.005)
            
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 1,65")
            return kills, losses, victory
        ##########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton2.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 2")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 2,65")
            return kills, losses, victory
        ###########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton3.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 3")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 3,65")
            return kills, losses, victory
        ############################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton4.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 4")
            
        time.sleep(0.005)
                                
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 4,65")
            return kills, losses, victory
        ###############################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton5.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 5")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 5,65")
            return kills, losses, victory
        ##################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton6.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 6")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 6,65")
            return kills, losses, victory
        #####################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton7.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 7")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 7,65")
            return kills, losses, victory
        ####################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton8.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 8")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 8,65")
            return kills, losses, victory
        ###################################3
        x = MI.locateCenterOnScreen('images/xButton/xbutton9.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 9")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 9,65")
            return kills, losses, victory
        #####################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton10.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 10")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 10,65")
            return kills, losses, victory
        ###########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton11.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 11")
            
        time.sleep(0.005)
                                
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 11,65")
            return kills, losses, victory
        #############################################3
        x = MI.locateCenterOnScreen('images/xButton/xbutton12.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 12")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 12,65")
            return kills, losses, victory
        #####################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton13.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 13")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 13,65")
            return kills, losses, victory
        ################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton14.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 14")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 14,65")
            return kills, losses, victory
        #####################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton15.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 15")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 15,65")
            return kills, losses, victory
        #####################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton16.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 16")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 16,65")
            return kills, losses, victory
        #########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton17.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 17")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 17,65")
            return kills, losses, victory
        ###########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton18.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 18")
            
        time.sleep(0.005)
                              
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 18,65")
            return kills, losses, victory
        ################################################  
        x = MI.locateCenterOnScreen('images/xButton/xbutton19.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 19")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 19,65")
            return kills, losses, victory
        ###############################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton20.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 20")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 20,65")
            return kills, losses, victory
        ################################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton21.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 21")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 21,65")
            return kills, losses, victory
        ################################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton22.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 22")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 22,65")
            return kills, losses, victory
        #####################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton23.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 23")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 23,65")
            return kills, losses, victory
        #########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton24.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 24")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 24,65")
            return kills, losses, victory
        ##############################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton25.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 25")
            
        time.sleep(0.005)
                             
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 25,65")
            return kills, losses, victory
        #########################################################   
        x = MI.locateCenterOnScreen('images/xButton/xbutton26.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 26")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 26,65")
            return kills, losses, victory
        ################################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton27.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 27")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button 27,65:")
            return kills, losses, victory
        ##########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton28.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 28")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 28,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton29.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 29")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 29,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton30.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 30")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 30,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton31.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 31")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 31,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton32.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 32")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 32,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton33.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 33")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 33,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton34.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 34")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 34,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton35.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 35")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 35,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton36.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 36")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 36,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton37.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 37")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 37,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton38.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 38")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 38,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton39.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 39")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 39,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton40.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 40")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
                   pass
        else:
            print("\n\tCorrect X button: 40,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton41.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 41")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 41,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton42.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 42")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 42,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton43.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 43")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 43,65")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton44.png', confidence = 0.65, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 44")
            
        time.sleep(0.1)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 44,65")
            return kills, losses, victory

        print("\nFailed with 65 confidence")
        print("\tConfidence -15\n")
        #print("\tX Buttons found:\n")
        
##############################################################
##############################################################
##############################################################
##############################################################
##############################################################
##############################################################

        x = MI.locateCenterOnScreen('images/xButton/xbutton1.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 1")
            
        time.sleep(0.005)
            
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 1,55")
            return kills, losses, victory
        ##########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton2.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 2")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 2,55")
            return kills, losses, victory
        ###########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton3.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 3")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 3,55")
            return kills, losses, victory
        ############################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton4.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 4")
            
        time.sleep(0.005)
                                
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 4,55")
            return kills, losses, victory
        ###############################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton5.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 5")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 5,55")
            return kills, losses, victory
        ##################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton6.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 6")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 6,55")
            return kills, losses, victory
        #####################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton7.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 7")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 7,55")
            return kills, losses, victory
        ####################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton8.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 8")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 8,55")
            return kills, losses, victory
        ###################################3
        x = MI.locateCenterOnScreen('images/xButton/xbutton9.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 9")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 9,55")
            return kills, losses, victory
        #####################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton10.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 10")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 10,55")
            return kills, losses, victory
        ###########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton11.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 11")
            
        time.sleep(0.005)
                                
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 11,55")
            return kills, losses, victory
        #############################################3
        x = MI.locateCenterOnScreen('images/xButton/xbutton12.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 12")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 12,55")
            return kills, losses, victory
        #####################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton13.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 13")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 13,55")
            return kills, losses, victory
        ################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton14.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 14")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 14,55")
            return kills, losses, victory
        #####################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton15.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 15")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 15,55")
            return kills, losses, victory
        #####################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton16.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 16")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 16,55")
            return kills, losses, victory
        #########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton17.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 17")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 17,55")
            return kills, losses, victory
        ###########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton18.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 18")
            
        time.sleep(0.005)
                              
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 18,55")
            return kills, losses, victory
        ################################################  
        x = MI.locateCenterOnScreen('images/xButton/xbutton19.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 19")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 19,55")
            return kills, losses, victory
        ###############################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton20.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 20")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 20,55")
            return kills, losses, victory
        ################################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton21.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 21")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 21,55")
            return kills, losses, victory
        ################################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton22.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 22")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 22,55")
            return kills, losses, victory
        #####################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton23.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 23")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 23,55")
            return kills, losses, victory
        #########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton24.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 24")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 24,55")
            return kills, losses, victory
        ##############################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton25.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 25")
            
        time.sleep(0.005)
                             
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 25,55")
            return kills, losses, victory
        #########################################################   
        x = MI.locateCenterOnScreen('images/xButton/xbutton26.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 26")
            
        time.sleep(0.005)
                        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 26,55")
            return kills, losses, victory
        ################################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton27.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 27")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 27,55")
            return kills, losses, victory
        ##########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton28.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 28")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 28,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton29.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 29")
            
        time.sleep(0.005)
                    
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 29,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton30.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 30")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 30,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton31.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 31")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 31,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton32.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 32")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 32,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton33.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 33")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 33,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton34.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 34")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 34,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton35.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 35")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 35,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton36.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 36")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 36,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton37.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 37")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 37,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton38.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 38")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 38,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton39.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 39")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 39,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton40.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 40")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 40,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton41.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 41")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 41,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton42.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 42")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 42,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton43.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 43")
            
        time.sleep(0.005)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 43,55")
            return kills, losses, victory
        ########################################
        x = MI.locateCenterOnScreen('images/xButton/xbutton44.png', confidence = 0.55, region = (960, 215, 960, 640))
        if(x):
            MI.click(x)
            #print("\tX Button Found 44")
            
        time.sleep(0.1)
        
        if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
            pass
        else:
            print("\n\tCorrect X button: 44,55")
            return kills, losses, victory

        #print("Failed with 55 confidence")

        playerSS = "images/xDetectErrors/DetectError" + "_" + str(time.time()) + ".png"
        MI.screenshot(playerSS, region = (960,215,960,640))
        print("X Button undetected")

        print('Starting, "Click Around"\n')

        if(MI.locateCenterOnScreen('images/didYouKnow.png', confidence = 0.75, region=(960, 215, 960, 640))):
            elaborateTime = time.time()
            MI.moveTo(1000, 300)
            while True:
                for j in range(45):
                    MI.move(20, 0)
                    MI.click()
                    time.sleep(0.005)

                    if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
                        pass
                    else:
                        print("\n\tCorrect X button found")
                        print("\tTime to find X:",math.floor(((time.time() - elaborateTime)%3600)/60), "minute(s), and", (round(((((time.time() - elaborateTime)%3600)/60)%1)*60,2,)), "second(s)")
                        time.sleep(0.5)
                        return kills, losses, victory
                    
                for p in range(1):
                    MI.move(0, 20)
                    MI.click()
                    time.sleep(0.005)

                    if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
                        pass
                    else:
                        print("\n\tCorrect X button found")
                        print("\tTime to find X:",math.floor(((time.time() - elaborateTime)%3600)/60), "minute(s), and", (round(((((time.time() - elaborateTime)%3600)/60)%1)*60,2,)), "second(s)")
                        time.sleep(0.5)
                        return kills, losses, victory
                    
                for k in range(45):
                    MI.move(-20, 0)
                    MI.click()
                    time.sleep(0.005)

                    if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
                        pass
                    else:
                        print("\n\tCorrect X button found")
                        print("\tTime to find X:",math.floor(((time.time() - elaborateTime)%3600)/60), "minute(s), and", (round(((((time.time() - elaborateTime)%3600)/60)%1)*60,2,)), "second(s)")
                        time.sleep(0.5)
                        return kills, losses, victory
                    
                for n in range(1):
                    MI.move(0, 20)
                    MI.click()
                    time.sleep(0.005)

                    if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
                        pass
                    else:
                        print("\n\tCorrect X button found")
                        print("\tTime to find X:",math.floor(((time.time() - elaborateTime)%3600)/60), "minute(s), and", (round(((((time.time() - elaborateTime)%3600)/60)%1)*60,2,)), "second(s)")
                        time.sleep(0.5)
                        return kills, losses, victory
        


