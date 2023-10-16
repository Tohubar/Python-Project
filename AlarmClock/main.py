from playsound import playsound
import os
import time

CLEAR = "\033[23"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    
    
    #print(CLEAR)
    os.system('cls')
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed +=1
        
        time_left = seconds - time_elapsed
        minute_left = time_left//60
        second_left = time_left%60
        print(f"{CLEAR_AND_RETURN}Alarm will ring in: {minute_left:02d}:{second_left:02d}")
    
    os.system('cls')
    print("Alarm is ringing")
    
    playsound("AlarmClock/alarm.mp3")
    
    os.system('cls')
    print("Finished ringing")


def ring_alarm():
    minutes = int(input("How many minutes to wait before alarm ring: "))
    second = int(input("How many seconds: "))
    total_time = minutes*60 + second

    alarm(total_time)
    
while True:
    ans = input("Do you want to start the Alarm (Y/N): ").lower() == "y"
    if not ans:
        break 
    ring_alarm()
    
