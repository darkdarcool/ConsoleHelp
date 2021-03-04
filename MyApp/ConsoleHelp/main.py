import time, sys
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'
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
def printcyan(text):
  print(CYAN + text + RESET)

def sp(text):
  for char in text:
    print(char, end = "")
    time.sleep(0.05)
    sys.stdout.flush()
def hello():
  print("Hello")
