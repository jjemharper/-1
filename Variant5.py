import random
 
def conjunction():
  return ", "+random.choice(conjunctions)
 
def noun(sex):
  if(sex == "m"):
    nouns = nouns1
  elif(sex == "f"):
    nouns = nouns2
  else:
    nouns = nouns3
 
  return random.choice(nouns)
 
def verb(time,sex):
  if(time == -1):
    if(sex == "m"):
      verbs = verbs1
    elif(sex == "f"):
      verbs = verbs2
    else:
      verbs = verbs3
  elif(time == 0):
    verbs = verbs4
  else:
    verbs = verbs5
 
  return random.choice(verbs)
 
def place(): 
  return random.choice(places)
 
def part_SSP():
  time = random.randint(-1,1)
  sex = random.choice(["m","f","x"])
  return noun(sex)+" "+verb(time,sex)+" "+place()
 
def SSP():
  return (part_SSP()+conjunction()+" "+part_SSP()+".").capitalize()
 
def IfSPP():
  sex1 = random.choice(["m","f","x"])
  sex2 = random.choice(["m","f","x"])
  return "если " + noun(sex1) +" "+ verb(random.randint(-1,1),sex1) +" "+ place() + ", " + noun(sex2)+" "+verb(1,sex2)
 
def TimeSPP():
  sex1 = random.choice(["m","f","x"])
  sex2 = random.choice(["m","f","x"])
  time = random.choice([-1,1])
  return "когда " + noun(sex1) +" "+ verb(time,sex1) + ", " + noun(sex2)+" "+verb(time,sex2)
 
 
def SPP():
  ver = random.randint(1,2)
  if (ver == 1):
    return (IfSPP()+".").capitalize()
  else:
    return (TimeSPP()+".").capitalize()





f = open('words.txt', 'r')
conjunctions = f.readline().replace("\n","").split(',')
nouns1 = f.readline().replace("\n","").split(',')
nouns2 = f.readline().replace("\n","").split(',')
nouns3 = f.readline().replace("\n","").split(',')
verbs1 = f.readline().replace("\n","").split(',')
verbs2 = f.readline().replace("\n","").split(',')
verbs3 = f.readline().replace("\n","").split(',')
verbs4 = f.readline().replace("\n","").split(',')
verbs5 = f.readline().replace("\n","").split(',')
places = f.readline().replace("\n","").split(',')

for i in range(random.randint(5,10)):
  sen = random.randint(1,2)
  if(sen==1):
    print(SPP())
  else:
    print(SSP())
