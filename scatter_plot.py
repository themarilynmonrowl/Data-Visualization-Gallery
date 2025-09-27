## Scatter Plot: Age vs Height ##
import seaborn as sns
import matplotlib.pyplot as plt

# use penguins dataset from seaborn library
df = sns.load_dataset("penguins").dropna()

# plot the figure
plt.figure(figsize=(8, 6))
plt.scatter(df["flipper_length_mm"], df["body_mass_g"], c="purple", alpha=0.6, edgecolors="k")
plt.title("Scatter Plot: Flipper Length vs Body Mass")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()
