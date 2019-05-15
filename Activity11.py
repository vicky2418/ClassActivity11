
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt

activity_data = pd.read_csv("tips.csv", index_col= 0)
print(activity_data)

female = activity_data[activity_data.sex == "Female"]
print(female)

male = activity_data[activity_data.sex == "Male"]
 

sum1 = female.groupby("day").sum()
print(sum1)

sum2 = male.groupby("day").sum()
print(sum2)

plt.plot(sum1.day, sum1.tip)
plt.plot(sum2.day, sum2.tip)
plt.legend(["Female", "Male"])
plt.xlabel("day")
plt.ylabel("tip")
plt.title("Tips per day")
plt.show()