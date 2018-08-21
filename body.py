import winsound
import time
import os
print(os.getcwd())
file_name = 'my_daily_data'
print(os.path.isfile(file_name))
work_time = 60
time.sleep(work_time)
sound_frequency = 2500  # Set Frequency To 2500 Hertz
sound_duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(sound_frequency, sound_duration)
print("hello")
