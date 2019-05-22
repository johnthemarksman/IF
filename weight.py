import time



### User entered data
#startDate = (2019, 5, 17, 13, 3, 39, 0, 137, 1)  #year, month, day
endDate = (2019, 5, 29)  #year, month, day
startingWeight = 173.2  
goalPerWeek = 3  #how many pounds you want to lose per week

goalPerDay = goalPerWeek/7
goalPerHour = goalPerDay/24

buffer = 2/24

currentWeight = float(input("Enter your current weight: "))

currentDate = time.localtime()

try:
    f = open("startDate.txt", "r")
    f.close()
    pass
except:
    f = open("startDate.txt", "w+")
    for i in currentDate:
        f.write(str(i) + ",")
    f.write("\n")
    #f.write(str(currentDate))
    f.close()
    pass

f = open("startDate.txt", "a+")
f.write(str(currentWeight)+","+str(currentDate[0])+","+str(currentDate[1])+","+str(currentDate[2])+","+"\n")
f.close()


f = open("startDate.txt", "r")
startDate = f.read().splitlines()[0].split(",")
f.close()

startDate.pop()
for i in range(len(startDate) - 1):
    startDate[i] = int(startDate[i])

    
print(startDate)
# print(currentDate)


requiredWeight = (startingWeight - (currentDate[7] - startDate[7])*goalPerDay)# + buffer*currentDate[3] + (buffer/60)*currentDate[4]
# if(currentWeight < requiredWeight):
#     print("you can eat", currentWeight, requiredWeight)
# else:
#     print("you can not eat", currentWeight, requiredWeight)


# i = (currentWeight - requiredWeight)/(buffer/60)
# print("You can eat in", i, "minutes")


#start of intermittent fasting
try:
    f = open("startDate.txt", "r")
    f.close()
    pass
except:
    f = open("startDate.txt", "w+")
    for i in currentDate:
        f.write(str(i) + ",")
    #f.write(str(currentDate))
    f.close()
    pass


fastPeriod = 8
maxDiff = 4
diffIntervals = maxDiff/fastPeriod

diff = currentWeight - requiredWeight

fastPeriod = fastPeriod - int(diff/diffIntervals)

print("you can eat for", fastPeriod, "hours today")





