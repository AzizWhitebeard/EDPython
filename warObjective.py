import pyautogui as MI
import time
MI.Pause = 0.001

warType = "fortune"
#You can find the war types;
#Right under this message.

warTypes = ["biodome", "wasteland", "naval", "barrens",
            "overlord", "infernal", "central", "fortune",
            "dread", "frysteland"]



def doWar(roomDone, checks, obMPX, obMPY, roomR, roomG, roomB):

    global warType
    global warTypes

    #Top of the epicduel game tab I think.
    obMPX = 1607
    obMPY = 18

    #Which objective on the map EX. LeftObjective.
    #whichSide = None #set to none because it will be used with any side
    #Not sure if I want to include this

    if roomDone == False:
        if warType.lower() in warTypes:




            ##### Central
            if warType.lower() == "central":
                if MI.locateCenterOnScreen('images/war/CentralRightOb.png', confidence=0.80, region=(1038, 415, 70, 70)):
                    obMPX = 1245
                    obMPY = 544
                    roomDone = True
                    checks+=1
                    roomR,roomG,roomB = MI.pixel(1348, 418)
                    return roomDone, checks, obMPX, obMPY, roomR, roomG, roomB
                elif MI.locateCenterOnScreen('images/war/CentralLeftOb.png', confidence=0.80, region=(969, 432, 230, 120)):
                    obMPX = 1435
                    obMPY = 527
                    roomDone = True
                    checks+=1
                    roomR,roomG,roomB = MI.pixel(1348, 418)
                    return roomDone, checks, obMPX, obMPY, roomR, roomG, roomB
                elif MI.locateCenterOnScreen('images/war/CentralMiddleOb.png', confidence=0.80, region=(1717, 465, 160, 160)):
                    obMPX = 1241
                    obMPY = 475
                    roomDone = True
                    checks+=1
                    roomR,roomG,roomB = MI.pixel(1348, 418)
                    return roomDone, checks, obMPX, obMPY, roomR, roomG, roomB
                else:
                    print("Couldn't find the supported images for CENTRAL war Type Either you're not in the room or its the wrong war type, see this in warObjective.py at the top")
                    checks = checks + 1
                    return roomDone, checks, obMPX, obMPY, roomR, roomG, roomB
            ##
            #
            #Fortune
            #
            #
            if warType.lower() == "fortune":
                if MI.locateCenterOnScreen('images/war/FortuneLeftOb.png', confidence=0.80, region=(1006, 225, 60, 60)):
                    obMPX = 1062
                    obMPY = 572
                    roomDone = True
                    checks+=1
                    roomR,roomG,roomB = MI.pixel(1348, 418)
                    MI.moveTo(1062, 572)
                    return roomDone, checks, obMPX, obMPY, roomR, roomG, roomB
                elif MI.locateCenterOnScreen('images/war/FortuneMiddleLeftOb.png', confidence=0.80, region=(992, 276, 65, 90)):
                    obMPX = 1117
                    obMPY = 487
                    roomDone = True
                    checks+=1
                    roomR,roomG,roomB = MI.pixel(1348, 418)
                    return roomDone, checks, obMPX, obMPY, roomR, roomG, roomB
                elif MI.locateCenterOnScreen('images/war/FortuneMiddleRightOb.png', confidence=0.80, region=(1355, 392, 105, 30)):
                    obMPX = 1767
                    obMPY = 538
                    roomDone = True
                    checks+=1
                    roomR,roomG,roomB = MI.pixel(1348, 418)
                    return roomDone, checks, obMPX, obMPY, roomR, roomG, roomB
                elif MI.locateCenterOnScreen('images/war/FortuneRightOb.png', confidence=0.80, region=(983, 284, 90, 60)):
                    obMPX = 1629
                    obMPY = 517
                    roomDone = True
                    checks+=1
                    roomR,roomG,roomB = MI.pixel(1348, 418)
                    return roomDone, checks, obMPX, obMPY, roomR, roomG, roomB
                else:
                    print("Couldn't find the supported images for FORTUNE war Type Either you're not in the room or its the wrong war type, see this in warObjective.py at the top")
                    checks = checks + 1
                    return roomDone, checks, obMPX, obMPY, roomR, roomG, roomB



                
        else:
            print("Error: WarType was not supported in warObjective.py")
            return roomDone, checks, obMPX, obMPY
    else:
        return roomDone, checks, obMPX, obMPY
