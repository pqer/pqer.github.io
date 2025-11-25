from processing import *


def setup():
  global appState, finalRound, score, periodNumber, movingScore, movingText, discoImage, lights, lighting
  appState = Starthomework
  size(500, 500)
  finalRound = False
  score = 0
  periodNumber = 0
  movingScore = 0
  movingText = 0
  lights = 0
  lighting = False
  
  discoImage = loadImage("Screenshot_2025-11-15_11.37.17_AM-removebg-preview.png")

def draw():
  appState()
  
def Starthomework():
  global score, periodNumber
  
  
  background(167, 177, 217)
  
  #Title
  textSize(50)
  fill(10, 33, 138)
  textAlign(CENTER, CENTER)
  text("Homework Timer", 250, 50)
  
  #start button
  fill(18, 199, 33)
  rect(162.5, 250, 175, 75)
  
  textSize(30)
  fill(0)
  textAlign(CENTER, CENTER)
  text("START", 250, 287.5)
  
  textSize(80)
  fill(0)
  textAlign(CENTER, CENTER)
  text("25:00", 250, 160)
  

def mouseReleased():
  import time
  global appState, Starthomework, secondsLeft, minutesLeft, timerRunning, periodNumber, score, startBreakTimer, timingBreak, start, finalRound, lights, lighting
  
  #click start button
  if appState == Starthomework:
    if 162.5 < mouseX < 337.5 and 250 < mouseY < 325:
      appState = timing
      start = time.time()
      timerRunning = 1
  
  elif appState == timing:
    if 162.5 < mouseX < 337.5 and 250 < mouseY < 325:
      #click I'm finished button
      if timerRunning == 1:
        appState = congrats
      #click next button
      elif timerRunning == 0:
        appState = Continue
  
  #productivity buttons
  elif appState == Continue:
    if finalRound == False:
      #top
      if 90 < mouseX < 135 and 125 < mouseY < 170:
        score += 1
        periodNumber += 1
        appState = startBreakTimer
      if 157.5 < mouseX < 202.5 and 125 < mouseY < 170:
        score += 2
        periodNumber += 1
        appState = startBreakTimer
      if 225 < mouseX < 270 and 125 < mouseY < 170:
        score += 3
        periodNumber += 1
        appState = startBreakTimer
      if 292.5 < mouseX < 337.5 and 125 < mouseY < 170:
        score += 4
        periodNumber += 1
        appState = startBreakTimer
      if 360 < mouseX < 405 and 125 < mouseY < 170:
        score += 5
        periodNumber += 1
        appState = startBreakTimer
      
      #bottom
      if 90 < mouseX < 135 and 192.5 < mouseY < 237.5:
        score += 6
        periodNumber += 1
        appState = startBreakTimer
      if 157.5 < mouseX < 202.5 and 192.5 < mouseY < 237.5:
        score += 7
        periodNumber += 1
        appState = startBreakTimer
      if 225 < mouseX < 270 and 192.5 < mouseY < 237.5:
        score += 8
        periodNumber += 1
        appState = startBreakTimer
        print("THIS SHOULDN't be happenning")
      if 292.5 < mouseX < 337.5 and 192.5 < mouseY < 237.5:
        score += 9
        periodNumber += 1
        appState = startBreakTimer
      if 360 < mouseX < 405 and 192.5 < mouseY < 237.5:
        score += 10
        periodNumber += 1
        appState = startBreakTimer
      
      
    elif finalRound == True:
      #top
      if 90 < mouseX < 135 and 125 < mouseY < 170:
        score += 1
        periodNumber += 1
        appState = displayStats
      if 157.5 < mouseX < 202.5 and 125 < mouseY < 170:
        score += 2
        periodNumber += 1
        appState = displayStats
      if 225 < mouseX < 270 and 125 < mouseY < 170:
        score += 3
        periodNumber += 1
        appState = displayStats
      if 292.5 < mouseX < 337.5 and 125 < mouseY < 170:
        score += 4
        periodNumber += 1
        appState = displayStats
      if 360 < mouseX < 405 and 125 < mouseY < 170:
        score += 5
        periodNumber += 1
        appState = displayStats
    
      #bottom
      if 90 < mouseX < 135 and 192.5 < mouseY < 237.5:
        score += 6
        periodNumber += 1
        appState = displayStats
      if 157.5 < mouseX < 202.5 and 192.5 < mouseY < 237.5:
        score += 7
        periodNumber += 1
        appState = displayStats
      if 225 < mouseX < 270 and 192.5 < mouseY < 237.5:
        score += 8
        periodNumber += 1
        appState = displayStats
        print("this shouldn't happen twice")
      if 292.5 < mouseX < 337.5 and 192.5 < mouseY < 237.5:
        score += 9
        periodNumber += 1
        appState = displayStats
      if 360 < mouseX < 405 and 192.5 < mouseY < 237.5:
        score += 10
        periodNumber += 1
        appState = displayStats
        
  elif appState == startBreakTimer:
    if 162.5 < mouseX < 337.5 and 250 < mouseY < 325:
      appState = timingBreak
      start = time.time()
      timerRunning = True
    
  elif appState == timingBreak:
    if 162.5 < mouseX < 337.5 and 250 < mouseY < 325:
      #click skip button
      if timerRunning == True:
        timerRunning = False
      #click next button
      elif timerRunning == False:
        appState = Starthomework
    if 365 <= mouseX <= 485 and 145 <= mouseY <= 265:
      if lighting == True:
        lighting = False
        print("clicked off")
      elif lighting == False:
        lighting = True
        print("clicked on")
  
  elif appState == congrats:
    if 162.5 < mouseX < 337.5 and 250 < mouseY < 325:
      appState = Continue
      finalRound = True
      

def timing():
  import time
  global start, minutesLeft, secondsLeft, ellapsedSeconds, timerRunning
  
  background(167, 177, 217)
  
  
  #Title
  textSize(50)
  fill(10, 33, 138)
  textAlign(CENTER, CENTER)
  text("Homework Timer", 250, 50)
  
  
  now = time.time()
  #1501
  minutesLeft = ((3 - (now - start))/60)
  
  ellapsedSeconds = ((now - start))
  
  secondsLeft = (3 - (now - start))%60
  
  #secondsLeft = 60 - (ellapsedSeconds)
  
 # if secondsLeft == 60:
  #  secondsLeft = 0
  

  #TIMER
  if timerRunning == 1:
    if minutesLeft >= 10 and secondsLeft >= 10:
      textSize(80)
      fill(0)
      textAlign(CENTER, CENTER)
      text(str(minutesLeft)[:2] + ":" + str(secondsLeft)[:2], 250, 160)
      print("A" + str(minutesLeft)[:2] + "," + str(secondsLeft)[:2])
    elif minutesLeft < 10 and secondsLeft >= 10:
      textSize(80)
      fill(0)
      textAlign(CENTER, CENTER)
      text("0" + str(minutesLeft)[:1] + ":" + str(secondsLeft)[:2], 250, 160)
      print("B" + str(minutesLeft)[:1] + "," + str(secondsLeft)[:2])
    elif minutesLeft >= 10 and secondsLeft < 10:
      textSize(80)
      fill(0)
      textAlign(CENTER, CENTER)
      text(str(minutesLeft)[:2] + ":0" + str(secondsLeft)[:1], 250, 160)
      print("C" + str(minutesLeft)[:2] + "," + str(secondsLeft)[:1])
    elif minutesLeft <= 1 and secondsLeft <= 1:
      #00:00
      textSize(80)
      fill(0)
      textAlign(CENTER, CENTER)
      text("00:00", 250, 160)
      print("E" + str(minutesLeft)[:2] + "," + str(secondsLeft)[:2])
      timerRunning = 0
    elif minutesLeft < 10 and secondsLeft < 10:
      textSize(80)
      fill(0)
      textAlign(CENTER, CENTER)
      text("0" + str(minutesLeft)[:1] + ":0" + str(secondsLeft)[:1], 250, 160)
      print("D" + str(minutesLeft)[:1] + "," + str(secondsLeft)[:1])
    
    #I finished! button
    fill(237, 33, 33)
    rect(162.5, 250, 175, 75)
  
    textSize(22)
    fill(0)
    textAlign(CENTER, CENTER)
    text("I Finished!", 250, 287.5)

  if timerRunning == 0:  
    #Next button
    fill(48, 89, 201)
    rect(162.5, 250, 175, 75)
    
    textSize(45)
    fill(0)
    textAlign(CENTER, CENTER)
    text("Next", 250, 287.5)
    
    #00:00
    textSize(80)
    fill(0)
    textAlign(CENTER, CENTER)
    text("00:00", 250, 160)
    
def congrats():
  background(167, 177, 217)
  
  
  #Title
  textSize(40)
  fill(10, 33, 138)
  textAlign(CENTER, CENTER)
  text("CONGRATULATIONS! \nYOU FINISHED!!!!", 250, 150)
  
  #Next button
  fill(48, 89, 201)
  rect(162.5, 250, 175, 75)
  
  textSize(45)
  fill(0)
  textAlign(CENTER, CENTER)
  text("Next", 250, 287.5)
  

def displayStats():
  global movingScore, movingText
  background(167, 177, 217)
  
  
  #Title
  textSize(30)
  fill(10, 33, 138)
  textAlign(CENTER, CENTER)
  text("Your average productivity score:", 250, 50)
  
  
  fill(167, 177, 217)
  rect(95, 150, 300, 60)
  rect(95, 150, 240, 60)
  rect(95, 150, 180, 60)
  rect(95, 150, 120, 60)
  rect(95, 150, 60, 60)
  
  fill(21, 107, 84, 200)
  rect(95, 150, (movingScore*30) - 3, 60)
  
  fill(0)
  textSize(14)
  textAlign(LEFT, TOP)
  text("Unproductive       Poor       Okay      Great      Extremely\n                                                                         Productive", 90, 215)

  fill(0)
  textSize(30)
  textAlign(CENTER, CENTER)
  text(str(movingText)[:3], 250, 95)
  
  if movingText < ((score/periodNumber) - 0.1):
    movingText += 0.1
  
  
  fill(0)
  textSize(20)
  textAlign(LEFT, TOP)
  text("0         2         4         6        8        10", 90, 125)
  
  if movingScore < (score/periodNumber):
    movingScore += 0.1

def Continue():
  background(167, 177, 217)
  
  #Title
  textSize(50)
  fill(10, 33, 138)
  textAlign(CENTER, CENTER)
  text("Homework Timer", 250, 50)
  
  textSize(13)
  fill(0)
  textAlign(CENTER, CENTER)
  text("From 1 to 10, how productive were you while working for this period of time? \n(1 being you got nothing done and 10 being you were as productive as possible) \nConsider the following questions when rating how productive you were: \nHow many problems did you get done? \nIs this an appropriate amount of work that you got done in that amount of time? \nHow much did you space out?", 250, 375)
  
  #buttons 1 - 10
  #top row
  fill(73, 148, 52)
  rect(90, 125, 45, 45)
  
  rect(157.5, 125, 45, 45)
  
  rect(225, 125, 45, 45)
  
  rect(292.5, 125, 45, 45)
  
  rect(360, 125, 45, 45)
  
  #bottom row
  rect(90, 192.5, 45, 45)
  
  rect(157.5, 192.5, 45, 45)
  
  rect(225, 192.5, 45, 45)
  
  rect(292.5, 192.5, 45, 45)
  
  rect(360, 192.5, 45, 45)
  
  #top text
  textSize(40)
  fill(225)
  textAlign(LEFT, TOP)
  text(" 1", 90, 125)
  
  text(" 2", 157.5, 125)
  
  text(" 3", 225, 125)
  
  text(" 4", 292.5, 125)
  
  text(" 5", 360, 125)
  
  #bottom text
  text(" 6", 90, 192.5)
  
  text(" 7", 157.5, 192.5)
  
  text(" 8", 225, 192.5)
  
  text(" 9", 292.5, 192.5)
  
  text("10", 360, 192.5)

def startBreakTimer():
  background(167, 177, 217)
  
  
  #Title
  textSize(50)
  fill(10, 33, 138)
  textAlign(CENTER, CENTER)
  text("Time to take a Break!", 250, 50)
  
  #start button
  fill(18, 199, 33)
  rect(162.5, 250, 175, 75)
  
  textSize(30)
  fill(0)
  textAlign(CENTER, CENTER)
  text("START", 250, 287.5)
  
  textSize(80)
  fill(0)
  textAlign(CENTER, CENTER)
  text("3:00", 250, 160)

def timingBreak():
  import time
  global timerRunning, lights, discoImage, lighting
  
  background(167, 177, 217)
  
  #Title
  textSize(50)
  fill(10, 33, 138)
  textAlign(CENTER, CENTER)
  text("Time to take a Break!", 250, 50)
  
  
  now = time.time()
  
  #180
  minutesLeft = ((31 - (now - start))/60)
  
  ellapsedSeconds = ((now - start))
  
  secondsLeft = (31 - (now - start))%60
  
  #TIMER
  if timerRunning == True:
    
    if lighting == True:
      if lights <= 1:
        background(224, 67, 67)
      elif lights <= 2:
        background(100, 209, 61)
      elif lights <= 3:
        background(143, 9, 184)
      elif lights <= 4:
        background(228, 232, 102)
      elif lights <= 5:
        background(102, 204, 232)
      elif lights <= 6:
        background(255, 117, 218)
        lights = 0
      
      lights += 0.06
      
    if minutesLeft < 10 and secondsLeft >= 10:
      textSize(80)
      fill(0)
      textAlign(CENTER, CENTER)
      text("0" + str(minutesLeft)[:1] + ":" + str(secondsLeft)[:2], 250, 160)
      #print("A" + str(minutesLeft)[:1] + "," + str(secondsLeft)[:2])
    elif minutesLeft <= 1 and secondsLeft <= 1:
      #00:00
      textSize(80)
      fill(0)
      textAlign(CENTER, CENTER)
      text("00:00", 250, 160)
      #print("B" + str(minutesLeft)[:2] + "," + str(secondsLeft)[:2])
      timerRunning = 0
    elif minutesLeft < 10 and secondsLeft < 10:
      textSize(80)
      fill(0)
      textAlign(CENTER, CENTER)
      text("0" + str(minutesLeft)[:1] + ":0" + str(secondsLeft)[:1], 250, 160)
      #print("C" + str(minutesLeft)[:1] + "," + str(secondsLeft)[:1])
    
    #skip button
    fill(237, 33, 33)
    rect(162.5, 250, 175, 75)
  
    textSize(25)
    fill(0)
    textAlign(CENTER, CENTER)
    text("Skip Break \n>>", 250, 287.5)
    
    textSize(15)
    fill(0)
    textAlign(CENTER, TOP)
    text("During you break feel free to:", 250, 350)
    textAlign(LEFT, TOP)
    text("-Relax, or lie down for a bit\n-take a little walk around the house\n-do a short chore\n-do ten jumping jacks, or some other short exercise\n-have a dance break", 100, 375)
    
    image(discoImage, 365, 145, 120, 120)
    textSize(15)
    fill(0)
    textAlign(CENTER, TOP)
    text("Click the disco ball!", 420, 265)
    
    #Title
    textSize(50)
    fill(10, 33, 138)
    textAlign(CENTER, CENTER)
    text("Time to take a Break!", 250, 50)
        
    
  if timerRunning == False:
    lighting = False
    
    #Next button
    fill(48, 89, 201)
    rect(162.5, 250, 175, 75)
    
    textSize(45)
    fill(0)
    textAlign(CENTER, CENTER)
    text("Next", 250, 287.5)
    
    #00:00
    textSize(80)
    fill(0)
    textAlign(CENTER, CENTER)
    text("00:00", 250, 160)
  
  # if appState == timing:
  #   if 162.5 < mouseX < 337.5 and 250 < mouseY < 325:
  #     if secondsLeft <= 0 and minutesLefft <= 0:
  #       appState = Next
  #     else:
  #       stoppedMinutesLeft = minutesLeft
  #       stoppedSecondsLeft = secondsLeft
  #       appState = done

run()
