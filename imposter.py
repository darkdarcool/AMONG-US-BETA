import os, time, random


time.sleep(1)
os.system('clear')
print('YOU ARE IMPOSTER')

tasks1 = [ "Formidable card swipe", "Enter ID code" ]
your_task1 = random.choice(tasks1)
task2 = ["clear Asteroid", "divert Power", "align telescope"]
your_task2 = random.choice(task2)
task3 = ["empty garbage.", 'fix wiring.']
your_task3 = random.choice(task3)



print('Your fake tasks are: ' + your_task1 + ', ' + your_task2 + ', ' + your_task3)