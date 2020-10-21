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
os.system('clear')
print(bwhite + 'Welcome to Among Us!\nBy:' +blue + ' darkdarcool')
print(white + 'a) Online\nb) Private(Coming soon)\nc) Update Log')
int = input(' ')
if int == "a":
  os.system("python3 loading.py")
elif int == "b":
  os.system("python3 private.py")
elif int == "c":
  os.system('python3 ulog.py')
else:
  print(red + 'INVALID COMMAND')
  time.sleep(2)
  os.system('clear')
  os.system('python3 home.py')