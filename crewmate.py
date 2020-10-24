import os, time, random
vote = 1
time.sleep(1)
os.system('clear')
print('YOU ARE CREWMATE')


tasks1 = [ "Formidable card swipe", "Enter ID code" ]
your_task1 = random.choice(tasks1)
task2 = ["clear Asteroid", "divert Power", "align telescope"]
your_task2 = random.choice(task2)
task3 = ["empty garbage.", 'fix wiring.']
your_task3 = random.choice(task3)
###########
#THE EMERGENCY MEETING#
def orange_bad():
  print('DISCUSS!')


print('Your tasks are: ' + your_task1 + ', ' + your_task2 + ', ' + your_task3 + '\nWrite anything you see in the rooms down!')
time.sleep(10)
def orange_imposter():
  os.system('clear')
  print('Position: Cafeteria\nEvery person has left to other rooms')
  print('Votes left: ' + str(vote))
  print('a) Left ')
  print('d) Right')
  print('w) Up   ')
  print('s) Down ')
  print('c) Stay ')
orange_imposter()

