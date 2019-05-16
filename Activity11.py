
import pandas as pd
import numpy as np
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

plt.bar(sum1.day, sum1.tip)
plt.bar(sum2.day, sum2.tip)
plt.legend(["Female", "Male"])
plt.xlabel("day")
plt.ylabel("tip")
plt.title("Tips per day")
plt.show()

correl = (activity_data.total_bill).corr(activity_data.size)
print(correl)

activity_data.per = (activity_data.tip / activity_data.totalbill) * 100
print(activity_data)