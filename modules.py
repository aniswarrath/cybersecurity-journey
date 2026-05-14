import datetime
today = datetime.date.today()
print(f"Today is:{today.strftime('%B %d, %Y')}")

import datetime
import random
import os

now = datetime.datetime.now()
print(f"Current time: {now.strftime('%H %M %S')}")

print(f"Random port: {random.randint(1, 65536)}")

print(f"log.txt exists: {os.path.exists('log.txt')}")