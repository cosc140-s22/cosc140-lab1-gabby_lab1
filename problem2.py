# Name: Gabriella Laines
#

import math

lat1 = float(input("What is the latitude of your first point? "))
lon1 = float(input("What is the longitude of your first point? "))
lat2 = float(input("What is the latitude of your second point? "))
lon2 = float(input("What is the longitude of your second point? "))

lat1 = math.radians(lat1)
lon1 = math.radians(lon1)
lat2 = math.radians(lat2)
lon2 = math.radians(lon2)

dlon = lon2-lon1
dlat = lat2-lat1
a = (math.sin(dlat/2))**2+math.cos(lat1) * math.cos(lat2) * (math.sin(dlon/2))**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
d_mi = 3956 * c
d_km = 6367 * c

print("The distance between the two points is", d_mi, "miles, or", d_km, "kilometers")