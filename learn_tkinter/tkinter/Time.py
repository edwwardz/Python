#21
import datetime as dt

x = dt.datetime.now()

print(x)

# 2
import time;

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
