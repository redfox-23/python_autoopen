#import things
import os
import datetime
#strings for os
q='*insert here the terminal command that starts your application1*'
w='*insert here the terminal command that starts your application2*'
#strings for the days of the week
mon='Mon'
tue='Tue'
wed='Wed'
thu='Thu'
fri='fri'
sat='Sat'
sun='Sun'
#grab the current date
x=datetime.datetime.now()
#string for storing the day in shortened format (eg Mon)
a=x.strftime("%a")
#prints out the current time
print(x)
#prints out the current day in shortened format
print(x.strftime("%a"))
#if statements to decide if we need to open the applicatos/applications
if a == mon or tue or wed or thu or fri:
    os.system(q)
if a == mon or tue or wed or thu or fri or sat or sun:
    os.system(w)
#of course you can have more apps
