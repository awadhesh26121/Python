import os
import pyttsx3
pyttsx3.speak("Welcome to my tools")
#print()
#print("Press 1: to open chrome browser")
#print("Press 2: to open notepad")
#print("Press 3: to opem media player")
print()

while True:
	
	
	print("Please enter your requirement else exit to end from my tools: ", end='')
	
	pyttsx3.speak("Please enter your requirement else exit to end from my tools")
	p=input()

	if ( "don't" in p or "dont" in p or ("do" in p and "not" in p )):
		print(" Ok, will not do that ")
	elif ( ("chrome" in p and "notepad" in p) or ("chrome" in p and ("media" in p or "player" in p)) or (("media" in p or "player" in p) and "notepad" in p )):
		pyttsx3.speak("Please access one program at a time") 
	elif (("run" in p or "open" in p) and ("chrome" in p or "browser" in p)):
		os.system("chrome")
	elif (("run" in p or "open" in p) and ("notepad" in p or "textpad" in p or "editor" in p)):
		os.system("notepad")
	elif (("run" in p or "open" in p) and ("media" in p or "player" in p)):
		os.system("wmplayer")
	elif ("exit" in p  or "quit" in p):
		break
	else:
		print("don't support")
