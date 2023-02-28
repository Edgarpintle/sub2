import datetime as dt

hoy = dt.date.today()

print(hoy)

fecNac = dt.date(2006,10,31)

print( fecNac )
print( fecNac.year )
print( fecNac.day)
print( fecNac.month)

print(f"{hoy: %A, %B, %d, %y}")

print(f"{hoy: %d/%m/%y}")

