import datetime
import os
GuyYear=int(os.environ['GuyYear'])
GuyMonth = int(os.environ['GuyMonth'])
GuyDay = int(os.environ['GuyDay'])
BethYear=int(os.environ['BethYear'])
BethMonth = int(os.environ['BethMonth'])
BethDay = int(os.environ['BethDay'])
DOBguy = datetime.datetime(GuyYear,GuyMonth,GuyDay)
Ageguy = (datetime.datetime.now() - DOBguy)
print("Guy is " + str(Ageguy.days) + " days old")
DOBbeth = datetime.datetime(BethYear,BethMonth,BethDay)
Agebeth = (datetime.datetime.now() - DOBbeth)
print("Beth is " + str(Agebeth.days) + " days old")
if Ageguy.days > Agebeth.days:
   DaysOlder = Ageguy.days - Agebeth.days
   print ("Guy is older by " + str(DaysOlder) + " days")
elif Agebeth.days > Ageguy.days:
   DaysOlder = Agebeth.days - Ageguy.days
   print ("Beth is older by " + str(DaysOlder) + " days")
