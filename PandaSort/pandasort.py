import pandas as pd

column_subset = [
    "id",
    "make",
    "model",
    "year",
    "cylinders",
    "fuelType",
    "trany",
    "mpgData",
    "city08",
    "highway08"
]

df = pd.read_csv(
    "https://www.fueleconomy.gov/feg/epadata/vehicles.csv",
    usecols=column_subset,
    nrows=100
)

print(df.head())
df = df.sort_values(
    by='city08'
    ,ascending=False
    ,kind='mergesort'
)
print(df.head())