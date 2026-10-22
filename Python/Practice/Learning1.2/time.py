time=int(input('give me a time:'))


time_hr=time//3600
time_min=time//60-time_hr*60
time_sec=time-time_hr*3600-time_min*60
print(time_hr, 'hrs', time_min, 'mins', time_sec, 's')