Steps on how to setup Jugg Script:
1. Download the zipped file from the github link: 
(The Link will download it for you!)

2. Open the zip file and drag the file to your desktop to get the unzipped version.

3. Install python 3.9.7(or higher) Link: https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe

4. Open up Windows Powershell (It will be needed to install the the script dependencies. 

5. Type the following things into Windows powershell:
	pip install pyautogui
	pip install Pillow (comment: caps matter)
	pip install opencv-python
	pip install keyboard
	pip install pyscreeze

6. Navigate to the folder where the scripts are held, click on the bar at the top that says "EDPython-Main", a
	Long file url will pop up that will dictate where the folder is located in your system. It should
	look a little something like this: C:\Users\USERNAME\Desktop\EDPython-main

7. Type in "cd C:\Users\USERNAME\Desktop\EDPython-main" in Windows Powershell to have windows powershell active in that folder.

8. Ensure your window resolution is 1980x1080p otherwise the script will not work.

9. Login into Epicduel, goto a  war objective(Where bombs are a dropped), hide somewhere, Turn on DND and goto a random world.

10. !!!VERY IMPORTANT!!! Drag the Epicduel window to the right side of the screen so that it is only covering half of the window screen.

11. Ensure you have the Epicduel Quality set to "Medium"!!!!!

12. Ensure you have the proper build setup with the proper cores. You may find the build in the following location:
	C:\Users\USERNAME\Desktop\EDPython-main\images
	
13. Type "python3 .\juggernautBH.py" in windows powershell to start the script! Enjoy!
13A If you want to steal energy, because npc's can now steal energy Put, "python3 .\juggernautBHStaticGrenade.py" in windows powershell too start the scipt! Enjoy!

FAQ: 
-Can I use different cores?
	*Yes you may, just make the tweaks to the proper areas in the script. new screenshot(s) of the cores will be needed. They can be
	found in the C:\Users\USERNAME\Desktop\EDPython-main\images\skills location.
	
-Do I need to use a war commander?
	*No, if you want to battle during the war without a war commander, just start the bot without a war commander!
	
-Does this work with Mac?
	*Yes, however the whole script will need a rework as well as new screenshots. Thought he logic will be the same.

-Does it target real players first?
	*Yes, it will use the strongest attacks against the player first.
	
-What if the script can't find the X button?
	*If the script cannot find the X button, it will take a screenshot of the end screen, you may add it to the array of images
	that will be used to find the X button. C:\Users\USERNAME\Desktop\EDPython-main\images\xDetectErrors
	if you add more x buttons, replace the other time.sleep(0.1) with time.sleep(0.005)
	also 	

-Can I still use my mouse on a different screen or on the other side of the screen?
	*Yes, though sometimes you can risk the script clicking something else accidentally.

-How do I stop the script?
	*Simply click on the windows power shell, and press CTRL+C on it. It should stop it. You also move your 
	mouse to one of the four corners of the screen.

-An image is not detected, help!
	*Go to the script and change the confidence to a lower number. No lower than .50

-I've been banned!
	*Thanks for playing the game, see ya in 7 days or more!
	
-None of these answer my question!!
	*Goto the README.md or READMETOO.md file(s) and go through it line by line to figure out your problem!