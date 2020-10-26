#Alarm Clock 
import time
import winsound
from datetime import datetime
now = datetime.now()
cur_time = now.strftime("%H:%M:%S")
H = int(now.strftime("%H"))
M = int(now.strftime("%M"))
print("This is current time", cur_time)
userInput = input("\n\n Enter the Name of Alaram: ")
user = datetime.strptime(input("Enter the time (in HHMM format) you want to set alarm: "),"%H%M")
print("Alarm set: ")
print(user.strftime("%H:%M\n"))
H1 = int(user.strftime("%H"))
M1 = int(user.strftime("%M"))
Diff_Hours = H1 - H
Diff_Min = M1 - M
if Diff_Min == 0:
    frequency = 3000
    duration = 50
    winsound.Beep((frequency, duration))
else:
    while True:
        now = datetime.now()
        time.sleep(1)
        if now.hour == H1:
            if now.minute == M1:
                print(userInput)
                frequency = 3000
                duration = 50
                winsound.Beep(frequency, duration)


