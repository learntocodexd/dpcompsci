"""
---------------------------------
THIS IS SO UGLY DP DONT JUDGE ME
---------------------------------

python3
print rabbit growth rate in pairs as they grow from babies to adults to a csv file
"""


def rabbits(startAdultRabbits, startBabyRabbits, monthlyReproductionRate, totalCages):

    adultRabbits = startAdultRabbits
    babyRabbits = startBabyRabbits
    rabbitCages = totalCages
    reproductionRate = monthlyReproductionRate
    tempBabyRabbits = 0
    totalRabbits = adultRabbits + babyRabbits

    print(babyRabbits, adultRabbits, totalRabbits)

    while totalRabbits < rabbitCages:
        tempBabyRabbits -= tempBabyRabbits #clear temp baby rabbits
        tempBabyRabbits += adultRabbits #adults making babies
        adultRabbits += babyRabbits #babies mature into adults
        babyRabbits -= babyRabbits #clear babies
        babyRabbits = tempBabyRabbits #temp babies to real babies
        totalRabbits = adultRabbits + babyRabbits #creating total
        print(babyRabbits, adultRabbits, totalRabbits)


rabbits(1, 0, 1, 500)
