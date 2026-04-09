import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df2 = pd.read_csv(r"C:/Users/keert/OneDrive/Documents/lab13.csv")
sns.pairplot(df2)
plt.show()
