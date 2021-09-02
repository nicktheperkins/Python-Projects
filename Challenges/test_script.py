import time
from datetime import datetime

# now = time.ctime(time.time())
# print(now)

now = datetime.now()

seconds_since_midnight = (now - now.replace(hour=0,minute=0,second=0,microsecond=0)).total_seconds()

print(now)
print(seconds_since_midnight)