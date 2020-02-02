# Priyanshu-CODERX
# Hacker's Terminal
# Created this just for time pass
# You can add more functions to it if you want


# NOTE: The dictionaryAttack function works so please don't use it for any bad



import time
import hashlib
import string
from random import *

def attacks():
	print("Type 'help' or 'Help' to access the help menu")
	while True:
		command = input("> ").lower()
		if command == "quit":
			print("Good Bye! HACKER")
			time.sleep(1.0)
			break
		elif command == "attacks":
			atks = "Attacks\n1. Brute-Force(1)\n2. Dictionary-Attack(2)\n3. Stegnography(3)\n"
			note = "NOTE: Use the special number given at the last of the attack name to access the attacks\n"
			print(atks)
			print(note)
		elif command == "about":
			print("Developer/Programmer: Priyanshu Bhattacharjee")
		elif command == "help":
			hlp = "Attacks: To access the attack features\nAbout: To know about the Developer\npgen: To Generate Passwords\nQuit: To quit the application"
			print(hlp)
		elif command == "1":
			# Calling Brute Force Attack in Attacks
			bruteFrc()
		elif command == "2":
			# Calling Dictionary Attack Function in Attacks
			dictionaryAttack()
		elif command == "3":
			# Calling Stegnography in Attacks
			stegno()
		elif command == "pgen":
			# Calling Password Generator function in Attacks
			passwordGen()

def loginSys():
	if usrnm == "testuser":
		if passwd == "testpass123":
			time.sleep(1)
			print("Logged in successfully....")
			time.sleep(0.5)
			# At first the loading scr will be called
			loadingScr()
			# After the loading scr the attacks function will be called
			attacks()
		else:
			print("Wrong password/username")
	else:
		print("Wrong password/username")

def dictionaryAttack():
	flag = 0

	pass_hash = input("Enter MD5 hash: ")

	wordlist = input("File name: ")

	try:
	    pass_file = open(wordlist, "r")
	except:
	    print("no file found")
	    quit()

	for word in pass_file:

	    enc_wrd = word.encode('utf-8')
	    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

	    #print(word)
	    #print(digest)
	    #print(pass_hash)

	    if digest == pass_hash:
	        print("Password found")
	        print("password is " + word)
	        flag = 1
	        break
	        

	if flag == 0:
	    print("password/passphrase is not in the list")

def passwordGen():
	letters = string.ascii_letters
	digits = string.digits
	symbols = string.punctuation
	chars = letters + digits + symbols

	min_length = 8
	max_length = 16
	password = "".join(choice(chars) for x in range(randint(min_length, max_length)))
	print("Your Password:",password)

def loadingScr():
	# This will be the loading screen for the program
	for i in range(10+1):
		load = f"Loading:{i}"
		time.sleep(0.3)
		print(load)

def stegno():
	print("Stegnography")

def bruteFrc():
	print("Brute Force")

#  execution point
print("Hackers Terminal")
time.sleep(0.5)
print("Welcome HACKER")
time.sleep(1)
usrnm = input("Username: ")
time.sleep(0.5)
passwd = input("Password: ")
time.sleep(0.5)

loginSys()
