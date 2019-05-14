# Exercise 2

# Satellites:

sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500,
                "GEOS"     : 2000,
                "worldview": 0.31
               }

# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]

# 2) print out all satellite names contained in the dictionary [2P]

print("I have the following satellites in my database:",list(sat_database))

# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]

answer_name = input("Please enter the satellite name from which you would like to know the resolution.")
if answer_name == "METEOSAT":
    print(3000)
elif answer_name == "LANDSAT":
    print(30)
elif answer_name == "MODIS":
    print(500)
elif answer_name == "GEOS":
    print(2000)
elif answer_name == "worldview":
    print(0.31)

# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]

answer_name = input("Please enter the satellite name from which you would like to know the resolution.")
if answer_name in sat_database:
    print("The satellite is in the database.")
else:
    print("Sorry! The satellite is not in the database.")

# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P] 

answer_name = input("Please enter the satellite name from which you would like to know the resolution.")
if answer_name in sat_database:
    for key, val in sat_database.items():
        print("Satellite {} has a resolution {} meters.".format(key, val))

else:
    print("Sorry! The satellite is not in the database")
