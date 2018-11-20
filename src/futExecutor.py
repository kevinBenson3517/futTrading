from time import sleep
from threading import Thread

MAX_TPS_HOUR= 500
MAX_TPS_DAY= 5000
# Wrapper for the fut script to run for specified time. 
def run_fut(duration):
    sleep(1)

hoursToRun = int(input('Enter the amount of hours you want to run this: '))
if hoursToRun <= 10:
    maxTPSHour = MAX_TPS_HOUR
if 10 < hoursToRun < 24:
    maxTPSHour = MAX_TPS_DAY/hoursToRun
if 24 < hoursToRun:
    maxTPSHour = 208

t = Thread(target=run_fut, args=(maxTPSHour))   # run the fut func in another thread. 
t.daemon = True                                 # Python will exit when the main thread
                                                # exits, even if this thread is still
                                                # running

t.start()
secondsToRun = hoursToRun*3600
sleep(secondsToRun)