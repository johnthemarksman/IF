import time
### User entered data
startDate = (2019, 5, 17, 13, 3, 39, 0, 137, 1)  #year, month, day
endDate = (2019, 5, 29)  #year, month, day
startingWeight = 173.2  
goalPerWeek = 3  #how many pounds you want to lose per week

goalPerDay = goalPerWeek/7
goalPerHour = goalPerDay/24

buffer = 2/24

currentWeight = float(input("Enter your current weight: "))

currentDate = time.localtime()

#print(currentDate)


requiredWeight = (startingWeight - (currentDate[7] - startDate[7])*goalPerDay) + buffer*currentDate[3] + (buffer/60)*currentDate[4]

if(currentWeight < requiredWeight):
    print("you can eat", currentWeight, requiredWeight)
else:
    print("you can not eat", currentWeight, requiredWeight)


i = (currentWeight - requiredWeight)/(buffer/60)

print("You can eat in", i, "minutes")
