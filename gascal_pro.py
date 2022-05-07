"""Importing all modules"""

import pandas as pd
import csv
from datetime import date

"""Setting Date for storing in CSV file"""

today = date.today()
d = today.strftime("%d/%m/%Y")

"""Inputing all arguments"""

previousReading = int(input("Enter Previous Reading : "))
currentReading = int(input("Enter Current Reading : "))
rplpg = float(input("Enter Rate Per Unit Of LPG : "))

"""Calculating Units Consumed and Total Amount"""

ta = (currentReading - previousReading) * rplpg
uc = (currentReading - previousReading)

"""Creating Header"""
headerList = ["Date", "Previous Reading", "Current Reading", "Rate/Unit of LPG", "Units Consumed", "Total Amount"]

"""Storing values in Pandas DataFrame"""
data = pd.DataFrame([
        d,
        previousReading,
        currentReading,
        rplpg,
        uc,
        ta
    ])

"""Writing to CSV file"""

data.to_csv('/Gascal.csv', mode='a',index=False, header=headerList)