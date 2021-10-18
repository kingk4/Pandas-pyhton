import pandas as pd

pd = pd.read_csv('C:/Users/Administrator/PycharmProjects/haider.csv')

print(pd.head())  #First 5-10 lines are shown !!
print("--------------------------------------")

print(pd.tail())   # last lines are shown !!
print("--------------------------------------")

print(pd)  # Showing full csv_file !!
print("--------------------------------------")
