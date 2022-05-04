# Importing CSV module
import csv

# Importing Date Module and setting the date format
from datetime import date

today = date.today()
d = today.strftime("%d/%m/%Y")

# Getting the Input Values from the User
previousReading = int(input("Enter Previous Reading : "))
currentReading = int(input("Enter Current Reading : "))
rplpg = float(input("Enter Rate Per Unit Of LPG : "))

# Calculation of the Values
ta = (currentReading - previousReading) * rplpg
uc = (currentReading - previousReading)

# Storing Values in Dictionaries
key = [["Date"], ["Previous Reading"], ["Current Reading"], ["Rate Per Unit of LPG"], ["units Consumed"],
       ["Total Amount"]]
values = [[d], [previousReading], [currentReading], [rplpg], [uc], [ta]]

# Printing results in console
print("Total Amount : ₹", ta, "\n" + "Units Consumed : ", uc)

with open('Gascal.csv','a', encoding='UTF8', newline='') as file1:
    writer=csv.writer(file1)
    writer.writerow(key)

# Opening and Writing on CSV file
with open('Gascal.csv', 'a+', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
 #   writer.writerow(key)
    writer.writerow(values)
    file.close()
# Created by Aadarsh A.K on 24/04/2022 :)
