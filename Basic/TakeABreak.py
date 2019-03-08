#Wait for two hour
#open a browser
# put inside in the loop: 5 times

import webbrowser
import time

total_break=5
break_count=0
curr_time=time.ctime()

print ("start time = " + curr_time)

while break_count<total_break:
    time.sleep(5)
    url="http://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(url)
    break_count+=1
