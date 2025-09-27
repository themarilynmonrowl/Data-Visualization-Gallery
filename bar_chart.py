## Flights per Airline Company ##

import seaborn as sns
import matplotlib.pyplot as plt

# download the dataset from pre generated library
df = sns.load_dataset("flights")
flights_per_year = df.groupby("year")["passengers"].sum()

# plot the figure
plt.figure(figsize=(8, 6))
flights_per_year.plot(kind="bar", color="skyblue", edgecolor="k")
plt.title("Bar Chart: Total Flights per Year")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.show()
