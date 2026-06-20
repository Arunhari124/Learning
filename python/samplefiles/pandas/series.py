import pandas as pd

dict={"day1":1750,
      "day2":2100,
      "day3":1700}

series=pd.Series(dict)


print(series[series <= 2000])