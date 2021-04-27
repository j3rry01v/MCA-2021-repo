# write a programme to read specific columns of a given csv file and print the content of the column

import csv

header = ["place", "name", "age"]
with open("city.csv", "w") as file:
    write = csv.DictWriter(file, fieldnames=header)
    write.writeheader()
    write.writerow({"place": "Winterfell", "name": "Sansa", "age": 21})
    write.writerow({"place": "Bravos", "name": "Arya", "age": 21})
    write.writerow({"place": "Beyond wall", "name": "Robert", "age": 43})
    write.writerow({"place": "Sydney", "name": "Alderson", "age": 33})
with open("city.csv", "r") as file:
    read = csv.DictReader(file);
    n = input("Enter the column name you want(place,name,age):")
    for i in read:
        print(i[n])
