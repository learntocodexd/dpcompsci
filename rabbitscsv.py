"""

---------------   ---------------   ---------------   ---------------   ---------------   ---------------   
NAME IT main.py   NAME IT main.py   NAME IT main.py   NAME IT main.py   NAME IT main.py   NAME IT main.py   
---------------   ---------------   ---------------   ---------------   ---------------   ---------------   

python3
print rabbit growth rate in pairs as they grow from babies to adults to a csv file
"""


import csv


def csvrabbits():
    with open("rabbits.csv", "w", newline="") as f:
        thewriter = csv.writer(f)

        adultRabbits = 1
        babyRabbits = 0
        rabbitCages = 500
        reproductionRate = 1
        tempBabyRabbits = 0
        month = 1
        totalRabbits = adultRabbits + babyRabbits

        thewriter.writerow([month, adultRabbits, babyRabbits, totalRabbits])

        while totalRabbits < rabbitCages:
            tempBabyRabbits -= tempBabyRabbits #clear temp baby rabbits
            tempBabyRabbits = adultRabbits * reproductionRate #adults making babies
            adultRabbits += babyRabbits #babies mature into adults
            babyRabbits = tempBabyRabbits #temp babies to real babies
            totalRabbits = adultRabbits + babyRabbits #creating total
            month += 1
            thewriter.writerow([month, adultRabbits, babyRabbits, totalRabbits])

        f.close()
    print("csv file created")


if __name__ == '__main__':
    csvrabbits()
