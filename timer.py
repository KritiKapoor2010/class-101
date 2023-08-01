import time

def counter(seconds):
     
     mins=int(seconds/60)
     secs=int(seconds%60)
     timer=f'{mins}:{secs}'
     print(timer)
     

seconds = input("enter the time sec")
counter(int(seconds))



    
    
    