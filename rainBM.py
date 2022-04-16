import time
import pyautogui as MI
import random
import math
import finishBattle as CB
import warObjective as WAR

skype = False

warTime = True
wantWarCommander = True

killLimit = -1
maxBattles = 50

Human = False
PMFlag = False
WCFlag = False
#Don't touch ^^

turns = 0

#Top NPC Color
#(1111, 267, (179, 8, 8))

#Bottom NPC Color
#(1110, 376, (169, 9, 9))
seconds = 5
for i in range(seconds):
    print("Starting in", seconds)
    time.sleep(1)
    seconds-=1

def WCInsert():
    privateChat()

    time.sleep(0.2)

    print("\t\tAdding war commander\n")
    

    ##open inventory

    MI.click(1659, 833)

    time.sleep(2)

    slotempty = MI.locateCenterOnScreen('images/skills/slotempty.png', confidence = 0.85, region = (1720, 360, 70, 70))
    if slotempty:
            
        ##Click Slot

        MI.click(slotempty)
        time.sleep(1)

        ##Clicking on chat bar to search for warcommander

        MI.click(1801, 508)
        time.sleep(1)
        MI.write("War Commander", interval=0.05)

        time.sleep(2)

        #Clicking Wc
        commanderr = MI.locateCenterOnScreen('images/skills/warCommander.png', confidence=0.70, region=(1757, 526, 105, 25))
        if commanderr:
            MI.click(commanderr)

        ##Insert WC

        MI.click(1614,772)
        time.sleep(0.45)              

        ##Confirm Insert

        MI.click(1565,536)
        time.sleep(0.45)

        ##Close Inventory

        MI.click(1911,248)
        print("\t\tWar commander added\n")
        
    else:
        return


def mouseMove():
    MI.moveTo(1425, 365)
    privateChat()

def privateChat():
    global skype, PMFlag
    if MI.pixelMatchesColor(1208, 230, (3, 76, 122)):
        PMFlag = True
        statements = ["greetings", "hi", "hey", "good day", "hi-ya"]
        print("We have received a PM")
        playerSS = "images/PMs/" + "PM_" + str(time.time()) + ".png"
        MI.screenshot(playerSS, region = (960,215,960,640))
        
        if 1 > 0: #Don't want to indent
            #pause before clicking pm
            time.sleep(3)
            MI.click(1846, 237)
            time.sleep(1)
            #Clicks on the pm since its always in the same spot
            MI.click(1379, 548)
            MI.typewrite(random.choice(statements), interval=0.15)
            MI.hotkey("enter")
            if skype == True:
                if(MI.locateCenterOnScreen("images/smile.png", confidence=0.75, region=(6, 965, 946, 1020))):
                    MI.hotkey("ctrl", "prtscr")
                    MI.click(507, 999)
                    MI.hotkey("ctrl", "v")
                    time.sleep(0.25)
                    MI.click(854, 992)
                    MI.click(507, 999)
                    time.sleep(0.1)
                    MI.typewrite("PM")
                    time.sleep(0.35)
                    MI.hotkey("enter")
                else:
                    print("Couldn't find skype")
    else:
        return

#war commander bs

def warCommander():
    global WCFlag
    global turns
    global wantWarCommander
    if not wantWarCommander:
        return
    if(not WCFlag and turns == 0):
        WC = MI.locateCenterOnScreen('images/one.png', confidence = 0.70, region = (1067, 635, 15, 25))
        if(WC): 
            print("\t\tWC empty on next win\n")
            WCFlag = True

    return

def checkForHeal():
    #310-320, health heal
    r,g,b = MI.pixel(1792, 247)
    if(b <= 40):
        print("\t\tHealing\n")
        
        #Medic
        MI.click(MI.locateCenterOnScreen('images/skills/medic.png', confidence=0.70, region=(1021, 671, 825, 60)))

        #Health booster
        MI.click(1819, 622)

        mouseMove()

    return

def checkForHealHuman():
    #310-320, health heal
    r,g,b = MI.pixel(1792, 247)
    if(b <= 40):
        print("\t\tHealing against huaman(s)\n")
        
        #Medic
        MI.click(MI.locateCenterOnScreen('images/skills/medic.png', confidence=0.70, region=(1021, 671, 825, 60)))

        #Health booster
        MI.click(1819, 622)

        mouseMove()
    return


def withHumans(r,g,b, HumanTop, HumanBottom):
    global Human
    #Top NPC Color
    #(1111, 267, (177, 8, 8))

    #Bottom NPC Color
    #(1110, 376, (168, 10, 10))

    #Theres a human
    #Human is on top


    #Aux
    MI.click(1404, 634)

    #Bot right side
    MI.click(1682, 633)

    #Rain
    MI.click(MI.locateCenterOnScreen('images/rain.png', confidence=0.55, region=(1021, 671, 825, 60)))

    #Sidearm
    MI.click(1197, 634)

    #Strike
    MI.click(1403, 563)
    #Bottom NPC
    MI.click(1081, 653)
    #Top NPC
    MI.click(1170, 535)


    time.sleep(2.5)
    if HumanTop and HumanBottom:
        pass

    elif HumanTop:
        #Checking if human is still there
        if not MI.pixelMatchesColor(1111, 267,(r, g, b)):
            print("t\tDead Human Top\n")
    #Human is on bottom
    elif HumanBottom:
        #Checking if human is still there
        if not MI.pixelMatchesColor(1110, 376,(r, g, b)):
            print("\t\tDead Human Bottom\n")
    return r,g,b, HumanTop, HumanBottom

def noHumans(topNPCAlive, bottomNPCAlive):
    global turns
    #Detecting if NPC's are dead
    #Top NPC Color
    #(1111, 267, (177, 8, 8))


    #Aux
    MI.click(1404, 634)

    #Bot right side
    MI.click(1682, 633)

    #Rain
    MI.click(MI.locateCenterOnScreen('images/rain.png', confidence=0.55, region=(1021, 671, 825, 60)))

    #Sidearm
    MI.click(1197, 634)

    #Strike
    MI.click(1403, 563)
    #Bottom NPC
    MI.click(1081, 653)
    #Top NPC
    MI.click(1170, 535)

    #Bottom NPC Color
    #(1110, 376, (168, 10, 10))
    time.sleep(2.5)
    if not MI.pixelMatchesColor(1111, 267, (179, 8, 8)) and topNPCAlive:
        print("\t\tDead NPC Top in", turns, "turn(s)\n")
        topNPCAlive = False
    if not MI.pixelMatchesColor(1110, 376, (169, 9, 9)) and bottomNPCAlive:
        print("\t\tDead NPC Bottom in", turns, "turn(s)\n")
        bottomNPCAlive = False

    return topNPCAlive, bottomNPCAlive

def Jugg():
    PlayerFlag = False
    battleOver = False
    numPlayers = 0
    victory = False
    roomDone = False

    global skype
    global Human
    global warTime
    global PMFlag
    global WCFlag
    global warCommander
    global killLimit
    global maxBattles
    global turns

    numBattles = 0
    kills = 0
    losses = 0
    checks = 0

    startingTime = overallTime = time.time()

    while True:

        privateChat()

        inLobby = MI.locateCenterOnScreen('images/chatLog.png', confidence = 0.7, region = (1327, 817, 40, 35))
        if(inLobby):

            if warTime:
                if checks < 3 and not roomDone:
                    roomR = -12
                    roomG = -12
                    roomB = -12
                    roomDone = False
                    obMPX = 1607
                    obMPY = 18
                    roomDone, checks, obMPX, obMPY, roomR, roomG, roomB = WAR.doWar(roomDone, checks, obMPX, obMPY, roomR, roomG, roomB)
                elif MI.pixelMatchesColor(1348, 418, (roomR, roomG, roomB)):
                    MI.click(obMPX, obMPY)
                    time.sleep(0.25)
                    if MI.locateCenterOnScreen('images/skills/warX.png', confidence = 0.70, region=(1722, 397, 35, 35)):  
                        MI.click(1228,536)
                        time.sleep(0.25)
                        #Super war drop click area
                        if MI.locateCenterOnScreen('images/skills/warX.png', confidence = 0.70, region=(1722, 397, 35, 35)):
                            MI.click(1644,536)
                        else:
                            pass




            numBattles = numBattles + 1
            MI.click(1511, 831)

            time.sleep(1.2)

            #Keep pressing jugg if still there

            inLobbyy = MI.locateCenterOnScreen('images/chatLog.png', confidence = 0.7, region = (1327, 817, 40, 35))
            while(inLobbyy):
                MI.click(1511, 831)
                time.sleep(0.5)
                inLobbyy = MI.locateCenterOnScreen('images/chatLog.png', confidence = 0.7, region = (1327, 817, 40, 35))
                
            if(numBattles == 1):
                startingTime = overallTime = time.time()
            else:
                startingTime = time.time()

            print("Battle", numBattles)
            time.sleep(5)

            


        elif(MI.pixelMatchesColor(1888, 267, (0, 108, 227))):
            privateChat()
            HumanTop = False
            HumanBottom = False
            if 1 > 0:
                MI.click(1675, 835)
                MI.sleep(0.35)
                mouseMove()

                HumanTop = False
                HumanBottom = False

                #Top NPC Color
                #(1111, 267, (179, 8, 8))

                #Bottom NPC Color
                #(1110, 376, (169, 9, 9))

                #Top NPC
                if not (MI.pixelMatchesColor(1111, 267, (179, 8, 8))):

                    HumanTop = True
                    
                #Bottom NPC
                if not (MI.pixelMatchesColor(1110, 376, (169, 9, 9))):

                    HumanBottom = True

                #If human checking for pixel color because I am lazy to play 500 battles for a human on top :p
                #Hope you understand thank you for your consideration.
                if HumanTop and not HumanBottom:
                    r,g,b = MI.pixel(1111, 267)

                if HumanBottom and not HumanTop:
                    r,g,b = MI.pixel(1110, 376)
                
                
                if HumanTop or HumanBottom:
                    numPlayers = numPlayers + 1
                    print("\tReal Human", numPlayers, "\n") #Hopefully mod LOL
                    playerSS = "images/realPlayers/Player"+ str(numPlayers) + "_" + str(time.time()) + ".png"
                    MI.screenshot(playerSS, region = (960, 215, 960, 640))
                    if skype == True:
                        if(MI.locateCenterOnScreen("images/smile.png", confidence=0.75, region=(6, 965, 946, 1020))):
                            MI.hotkey("ctrl", "prtscr")
                            MI.click(507, 999)
                            MI.hotkey("ctrl", "v")
                            time.sleep(0.25)
                            MI.click(854, 992)
                            MI.click(507, 999)
                            time.sleep(0.1)
                            MI.typewrite("Non-Npc")
                            time.sleep(0.35)
                            MI.hotkey("enter")
                        else:
                            print("Couldn't find skype")
                    else:
                            pass

                    battleOver = True

            #Player Bubble
            topNPCAlive = True
            bottomNPCAlive = True
            while (MI.pixelMatchesColor(1888, 267, (0, 108, 227))):
                battleOver = True
                #STRIKE
                if(MI.pixelMatchesColor(1403, 563, (197, 177, 112))):
                    if HumanTop or HumanBottom:
                        if turns == 0:
                            warCommander()
                        turns=turns + 1
                        checkForHealHuman()
                        withHumans(r,g,b, HumanTop, HumanBottom)
                        privateChat()
                        mouseMove()
                    else:
                        if turns == 0:
                            warCommander()
                        turns=turns + 1
                        checkForHeal()
                        topNPCAlive, bottomNPCAlive = noHumans(topNPCAlive, bottomNPCAlive)
                        privateChat()
                        mouseMove()
                    

        else:
            if(warTime):
                drop = MI.locateCenterOnScreen('images/continue.png', confidence = 0.90, region = (1340,635,200,65))
                if(drop):
                    MI.click(drop)
                    
            if(battleOver):
                privateChat()
                if(MI.pixelMatchesColor(1042, 766, (255, 255, 76))):
                    kills, losses, victory = CB.finish(kills, losses)
                    if kills < 0 and losses < 0:
                        print("X undetected")
                        return
                    
                    if numBattles == 0:
                        kills = losses = 0 
                    Human = False
                    battleOver = False
                    NPCone = True
                    newTime = time.time()
                    if numBattles > 0:
                        battleStats(numBattles, kills, losses, newTime, startingTime, overallTime)
                    turns = 0
                    if WCFlag and victory:
                        WCInsert()
                        WCFlag = False
                    if PlayerFlag:
                        PlayerFlag = False
                    if PMFlag:
                        print("Done because PM")
                        return
                    if numBattles == maxBattles:
                        print("Reached quota of", maxBattles, "battle(s)")
                        return
                    if kills == killLimit:
                        print("Reached quota of", killLimit, "win(s)")
                        return


        
def battleStats(numBattles, kills, losses, newTime, startingTime, overallTime):
    global turns
    print("\n\t\tBattle Stats\n") 
    print("\t\t\tBattle time:",newTime - startingTime,"second(s)\n")
    print("\t\t\tTurns:",turns,"\n")     
    print("\t\t\tWins:",kills,"\n")          
    print("\t\t\tLosses:",losses,"\n")
    if kills or losses > 1:
        print("\t\t\tWin Percent:", (kills/(losses+kills))*100,"\n")
    print("\t\t\tPer hour wins with this time:", 3600/(newTime - startingTime), "win(s)\n")
    if(numBattles>1):
        print("\t\t\tAverage battle time:", (newTime - overallTime)/numBattles, "second(s)\n")
        if kills > 1:
            print("\t\t\tWins per hour:", 3600/((newTime - overallTime)/kills), "\n")
        print("\t\t\tTime spent battling:", math.floor((newTime - overallTime)/3600), "hour(s) and", ((newTime - overallTime)%3600)/60, "minute(s) \n\n")
    else:
        print("\t\t\tTime spent battling:", newTime - overallTime, "second(s)\n\n")


Jugg()
    



        



































    
        
