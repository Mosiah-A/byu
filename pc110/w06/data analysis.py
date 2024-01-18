'''
Author: Mosiah Andrade

Purpose: analysis data by Life-expectancy.csv

Added: add a code to calculate life expenctancy media by a year inputed  
'''

lowest_life = 100000000000000
highest_life = 0
year = 0
count = 0
le_sum = 0

with open("w06\life-expectancy.csv") as life_expetancy:
    media_year = int(input("What year do you want analyse: [1760-2019] "))
    
    for line in life_expetancy:
        line = line.split(",")
        if "Entity" != line[0]:
            entity = line[0]
            code = line[1]
            year = int(line[2])
            le = float(line[3])

            #lowest block
            if le < lowest_life:
                lowest_life = le
                lowest_country = entity
                lowest_year = year

            elif le > highest_life:
                highest_life = le
                highest_country = entity
                highest_year = year

            elif year == media_year:
                count += 1
                le_sum += le
                

    print(f"The overall max life expectancy is: {highest_life} from {highest_country} in {highest_year}")
    print(f"The Overall min life expentancy is: {lowest_life} from {lowest_country} in {lowest_year}")

    media = le_sum / count 
    print(f"Life expectancy Media by {media_year} is: {media:.2f}")