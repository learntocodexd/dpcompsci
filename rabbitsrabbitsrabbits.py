"""

-------------------------------------------------------------------------------------
THIS IS SO UGLY DP DONT JUDGE ME I WILL IMPLEMENT REPRODUCTION RATE CHANGES TOMORROW
-------------------------------------------------------------------------------------

python3
print rabbit growth rate in pairs as they grow from babies to adults to a csv file
"""


def rabbits(startAdultRabbits, startBabyRabbits, monthlyReproductionRate, totalCages):

    adultRabbits = startAdultRabbits
    babyRabbits = startBabyRabbits
    rabbitCages = totalCages
    reproductionRate = monthlyReproductionRate
    totalRabbits = adultRabbits + babyRabbits

    print(babyRabbits, adultRabbits, totalRabbits)

    while totalRabbits < rabbitCages:
        tempBabyRabbits = babyRabbits
        adultRabbits += tempBabyRabbits
        babyRabbits += adultRabbits
        totalRabbits = adultRabbits + babyRabbits
        print(babyRabbits, adultRabbits, totalRabbits)


rabbits(1, 0, 1, 500)
