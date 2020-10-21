import os,random, time


#colors

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bblack = "\033[0;90m"
bred = "\033[0;91m"
bgreen = "\033[0;92m"
byellow = "\033[0;93m"
bblue = "\033[0;94m"
bmagenta = "\033[0;95m"
bcyan = "\033[0;96m"
bwhite = "\033[0;97m"

time.sleep(1)
os.system('clear')
print(bwhite + 'Hello players! This is the Among Us beta game!! Updates will be constant updates to this game! The map will NOT be exact, but will almost be. Type any to begin the game!')

blank = ' '
inpt = input('')
if inpt == blank:
  os.system("python3 home.py")
elif input != blank:
	os.system("python3 home.py")