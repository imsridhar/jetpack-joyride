import numpy as numpy
import colorama
import os
from colorama import Style,Fore,Back

username = "Player"

quit_flag = 0
bullet_present = False
score = 0
lives = 5
dragon_lives = 10

os.system('tput reset')
print("Enter your name: ")
username = input()
os.system('tput reset')
    # config.create_banner()

class screen:
	def sky(self):
		print(Fore.BLUE + Back.BLACK,end="")
		for i in range(5):
			for j in range(140):
				print('#',end="")
			print()

	def play_area(self):
		print(Fore.RED + Back.BLACK,end="")
		for i in range(25):
			for j in range(140):
				print('0',end="")
			print()

	def ground(self):
		print(Fore.GREEN + Back.BLACK,end='')
		for i in range(8):
			for j in range(140):
				print('#',end="")
			print()			
obj=screen()
obj.sky()
print(Style.RESET_ALL,end='')		
obj.play_area()
print(Style.RESET_ALL,end='')
obj.ground()
print(Style.RESET_ALL)	