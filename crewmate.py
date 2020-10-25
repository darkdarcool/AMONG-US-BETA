import os, time, random
vote = 1
emer = 1
tasks_done = 0
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
print('YOU ARE CREWMATE')


tasks1 = [ "Formidable card swipe", "Enter ID code" ]
your_task1 = random.choice(tasks1)
task2 = ["clear Asteroid", "divert Power", "align telescope"]
your_task2 = random.choice(task2)
task3 = ["empty garbage.", 'fix wiring.']
your_task3 = random.choice(task3)
tasks1.remove(your_task1)
task2.remove(your_task2)
task3.remove(your_task3)

##########################
# THE EMERGENCY MEETINGS #
##########################
def orange_bad_emergency():
  print('DISCUSS!')


print('Your tasks are: ' + your_task1 + ', ' + your_task2 + ', ' + your_task3 + '\nWrite anything you see in the rooms down!')
time.sleep(15)
def orange_imposter():
  os.system('clear')
  print('Position: Cafeteria\nEvery person has left to other rooms')
  print('Tasks done: ' + str(tasks_done))
  print('Map: Null')
  print('Votes left: ' + str(vote))
  print('Emergency Meeting left: ' + str(emer))
  print('a) Left ')
  print('d) Right')
  print('w) Up   ')
  print('s) Down ')
  print('c) Stay ')
  print('p) Emegency Meeting')
  onerl = input(' ')
  if onerl == "a":
    time.sleep(1)
    os.system('clear')
    print('Moving. ')
    time.sleep(0.5)
    os.system('clear')
    print('Moving.. ')
    time.sleep(0.5)
    os.system('clear')
    print('Moving... ')
orange_imposter()

