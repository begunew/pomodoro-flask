import time
from playsound import playsound

# personal pomodoro

# sets of intense focus, adjustable time, ring/notification, immediate rest time

pomodoro = 25
break_time = 5
print("Welcome to Pomdoro!\nDefault pomodoro: 25min.\n========================")

def run_pomodoro(minute):
  second = 00
  
  while (minute != 00 or second != 00):
    if second == 00:
      minute -= 1
      second = 60

    second-=1
    time.sleep(1)
    print(str(minute) + ":" + str(second))
  print("Time is finished!")
  playsound('./audio/notification.mp3')

def full_set():
  print("First set:")
  run_pomodoro(pomodoro)
  print("Second set:")
  run_pomodoro(break_time)
  print("Third set:")
  run_pomodoro(pomodoro)
  print("Fourth set:")
  run_pomodoro(break_time)

if __name__ == "__main__":
  full_set()