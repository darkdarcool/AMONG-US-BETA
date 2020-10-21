import os, random, time

ci = random.randint(1, 2)
if ci == 1:
  os.system("python3 imposter.py")
elif ci == 2:
  os.system("python3 crewmate.py")