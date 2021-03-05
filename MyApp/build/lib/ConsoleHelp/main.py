import time, sys, os
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'
ORANGE = '\033[0;33m'
RESET = '\033[0m'
def orange():
  return ORANGE
def red():
  return RED
def green():
  return GREEN
def yellow():
def ysn():
  print("[y/n]", end = "")
  return YELLOW
def blue():
  return BLUE
def magenta():
  return MAGENTA
def cyan():
  return CYAN
def white():
  return WHITE
def underline():
  return UNDERLINE
def normal():
  return RESET
def printred(text):
  print(RED + text + RESET)
def printgreen(text):
  print(GREEN + text + RESET)
def printyellow(text):
  print(YELLOW + text + RESET)
def printblue(text):
  print(BLUE + text + RESET)
def printmagenta(text):
  print(MAGENTA + text + RESET)
def printorange(text):
  print(ORANGE + text + RESET)
def printcyan(text):
  print(CYAN + text + RESET)
def printunderline(text):
  print(UNDERLINE + text + RESET)

def sp(text):
  for char in text:
    print(char, end = "")
    time.sleep(0.05)
    sys.stdout.flush()
def clear():
  print("\033c", end = "")

class color():
  def spc(text,color = None): # put try statement
    sun = 0
    if color == None:
      print("Please do fill out the color text box")
      sun = 1
    if sun == 0:
      elif color == "red":
        for char in text:
          print(RED + char, end = "")
          time.sleep(0.05)
          sys.stdout.flush()
      elif color == 'orange':
        for char in text:
          print(ORANGE + char, end = "")
          time.sleep(0.05)
          sys.stdout.flush()
      elif color == 'green': 
        for char in text:
          print(GREEN + char, end = "")
          time.sleep(0.05)
          sys.stdout.flush()
      elif color == 'blue': 
        for char in text:
          print(BLUE + char, end = "")
          time.sleep(0.05)
          sys.stdout.flush()
      elif color == 'yellow': 
        for char in text:
          print(YELLOW + char, end = "")
          time.sleep(0.05)
          sys.stdout.flush()
      elif color == 'magenta': 
        for char in text:
          print(MAGENTA + char, end = "")
          time.sleep(0.05)
          sys.stdout.flush()
      elif color == 'cyan': 
        for char in text:
          print(CYAN + char, end = "")
          time.sleep(0.05)
          sys.stdout.flush()
      elif color == 'underline': 
        for char in text:
          print(UNDERLINE + char, end = "")
          time.sleep(0.05)
          sys.stdout.flush()
      else:
        print(f'Error: unknown text formatting: {color}')#lol
   else:
     pass

#hahahahahahhahahah
