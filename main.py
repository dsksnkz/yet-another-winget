import random
import progressbar
import time
import getpass




corespeed=(random.uniform(0.1,0.002))
extraspeed=(random.uniform(0.1,0.002))
multilibspeed=(random.uniform(0.1,0.002))


pwd=("    ")
pwdinput = getpass.getpass("[sudo] password for user: ")



def startyaw():

    if pwdinput == pwd:
    
    
    
    
        print(":: Synchronizing package databases...")
    
        b = progressbar.ProgressBar(maxval=100)
    
        b.start()
        print("core","                1.0 MB   ", round(corespeed*100), "KB/s" )
        try:
           for i in range(100):
               time.sleep(corespeed)
               b.update(i + 1)
        except KeyboardInterrupt:
               print("\nyaw interrupted")
        b.finish()
    
    
    
        b = progressbar.ProgressBar(maxval=100)
    
        b.start()
        print("extra","                1.0 MB   ", round(extraspeed*100), "KB/s" )
        try:
           for i in range(100):
               time.sleep(extraspeed)
               b.update(i + 1)
        except KeyboardInterrupt:
               print("\nyaw interrupted")
        b.finish()
    
    
    
    
    
        b = progressbar.ProgressBar(maxval=100)
    
        b.start()
        print("multilib","                1.0 MB   ", round(extraspeed*100), "KB/s" )
        try:
           for i in range(100):
               time.sleep(multilibspeed)
               b.update(i + 1)
        except KeyboardInterrupt:
               print("\nyaw interrupted")
        b.finish()
    
    
    
    else:
        time.sleep(1)
        print("[sudo] password for user: Sudo password incorrect")
        startyaw()                            
    
startyaw()
