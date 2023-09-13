from artwork import logo,vs,gameOver
from dataset import data
import random
import os

def dataPrinter(dataA,dataB):
  print(logo)
  print(f"Compare A: {dataFormatter(dataA)}")
  print(vs)
  print(f"Compare B: {dataFormatter(dataB)}")
   
def randomDataGenerator():
    return random.choice(data)

def dataFormatter(details):
  name = details["name"]
  desc =  details["description"]
  country = details["country"]
  return f"{name}, a {desc}, from {country}"

dataA = randomDataGenerator()
dataB = randomDataGenerator()
dataPrinter(dataA,dataB)

score = 0
gameContinue = True
while(gameContinue):
  choice = input("Who has more followers ? Type A or B :")
  followersA = dataA["follower_count"]
  followersB = dataB["follower_count"]


  if(choice == "A" and followersA > followersB):
    score += 1
    os.system('cls')
    print(f"You're right ! Current Score : {score}")
    dataA = dataB
    dataB = randomDataGenerator()
    dataPrinter(dataA,dataB)
  elif(choice == "B" and followersA < followersB):
    score += 1
    os.system('cls')
    print(f"You're right ! Current Score : {score}")
    dataB = randomDataGenerator()
    dataPrinter(dataA,dataB)  
  else:
    os.system('cls')
    print(gameOver)
    print(f"Sorry, that's wrong. Final score : {score}")
    gameContinue = False 

    


