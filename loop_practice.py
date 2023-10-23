# Loop Practice
# Author : William
# Date : 10 October 2023

# Promblem
# create a new year eve countdown that's automated
# Requuirements:
# - starts at 10 
# - counts down every second printing the second it's at
# instead of reaching zero, it prints out "Happy New year"

import time 

for number in range(10,0,-1):
    print(number)
    time.sleep(1)
print("Happy New Year!")



