#Liam Collins
#4/26/18
#displayDate.py

from datetime import date

today = date.today()

months = ['January','February','March','April','May','June','July','August','September','October','November','December']
weeks = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

print('Today is',weeks[today.weekday()], ',',months[today.month-1],today.day,today.year)
