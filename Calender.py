#Example file for working with calenders.
#import the calender module.

import calendar

#Create a plain text calender
c = calendar.TextCalendar(calendar.SUNDAY)
#st = c.formatmonth(2025, 1, 0, 0)
#print(st)


#Create HTML formated calendar
#hc= calendar.HTMLCalendar(calendar.SUNDAY)
#st = hc.formatmonth(2025, 1)
#print(st)

#loop over the days of the month
#zeroes mean that the day of the week is an overlapping month 

for i in c.itermonthdays(2025, 1):
    print(i)
#
#use calendar import module to print months and days
#for name in calendar.month_name:
    #print(name)


    #for day in calendar.day_name:
        #print(day)

   #Calculate days based on a rule: Example, consider
   #a team meeting on the first Friday of every month,
   # To figure out what days that would be each month
   # we can use this script
print("Team meetings will be on: ") 
for m in range (1,13):
    cal = calendar.monthcalendar(2025, m)
    weekone=cal[0]
    weektwo=cal[1]

    if weekone[calendar.FRIDAY] !=0:
        meetday = weektwo[calendar.FRIDAY]

        print("%10s %2d" % (calendar.month_name[m], meetday))

      








