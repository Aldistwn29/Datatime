import datetime as dt
tgl_lahir = dt.datetime(2003, 3, 29)
date_string = tgl_lahir.strftime("%d %B %y")
print(date_string)