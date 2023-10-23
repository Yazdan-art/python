hour=float(input("please enter time  "))
rate=float(input("please enter rate  "))

def normal_sallary():
 return hour*rate

def over_time():
 return float(hour-160)
  
def over_sallary(over_time):
 return (160*rate)+(over_time*rate*1.5)
#____________________________  
if hour<=160 :
  print (normal_sallary())
else:
 print(over_sallary(over_time()))