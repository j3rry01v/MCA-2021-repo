#purpose - to find leap years of future year from current year
#author : jerry
startYear = 2021
print ("Enter any future year")
endYear = int(input())
 
print ("List of leap years:")
for year in range(startYear, endYear):
  if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
    print (year)