import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'df' is a DataFrame
# with columns 'x', 'y', 'z'
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5, 6, 7, 8],
    'y': [2, 4, 3, 7, 6, 9, 8, 12],
    'z': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B'],
})

sns.scatterplot(x='x', y='y', hue='z', data=df)
plt.show()