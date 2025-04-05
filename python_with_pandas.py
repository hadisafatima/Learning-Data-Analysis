import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

netflix = pd.read_csv(r'C:\Users\HP\Downloads\netflix_titles.csv')
print(netflix.head())
# print(netflix.shape)
# print(netflix.info())
# print(netflix.describe())
# print(netflix['release_year'].median())

# print(netflix['release_year'].value_counts().plot(kind="hist", figsize=(10, 10)))
print(netflix.value_counts())
print(netflix.loc[netflix['type'] == 'Movie', 'country'].mean())
plt.show()


# have to keep following the yt video 

# pausing the yt video and giving time to create a databse in MySQL