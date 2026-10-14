import random
import progressbar
import time
import getpass


corespeed=random.uniform(0.02,0.1)

print(corespeed)
print(":: Synchronizing package databases...")
    
b = progressbar.ProgressBar(maxval=100)

b.start()

print("core           150.2 KiB   ", round(corespeed*100), "KB/s" )

try:
   for i in range(100):
       time.sleep(corespeed)
       b.update(i + 1)
except KeyboardInterrupt:
       print("\nyaw interrupted")

b.finish()

b = progressbar.ProgressBar(maxval=100)

b.start()

print("core                     150.2 KiB   ", )

try:
   for i in range(100):
       time.sleep(0.1)
       b.update(i + 1)
except KeyboardInterrupt:
       print("\nyaw interrupted")

b.finish()




