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

"""Storing values in Pandas DataFrame"""
data = pd.DataFrame(
    {
        'Date':[d],
        'Previous Reading':[previousReading],
        'Current Reading':[currentReading],
        'Rate/Unit of LPG':[rplpg],
        'Units Consumed':[uc],
        'Total Amount':[ta]
    })

"""Writing to CSV file"""

data.to_csv('/Gascal.csv', mode='a',index=False, header=False)