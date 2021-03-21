#i tried using zellers, you can see that i am no longer using zellers
from datetime import date

count = 0
for year in range(1901,2001):
    for month in range(1,13):
        day = date(year, month, 1).isoweekday()
        if day == 7:
            count += 1
print(count)
