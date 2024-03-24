#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Create boxplots to visualize the distribution of each feature within each species
sns.boxplot(
    x = "species",
    y = "sepal_length",
    showmeans=True,
    data=data
)
plt.title("Sepal Length Distribution by Species")
plt.show()

# Repeat for other features (sepal_width, petal_length, petal_width)


# In[3]:


import pandas as pd

# Load Iris flower dataset from UCI repository
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = pd.read_csv(url, names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])


# In[4]:


# Get basic information about the data (number of rows, columns, data types)
print(data.info())

# Display the first few rows of the data
print(data.head())

# Summarize numerical features (mean, standard deviation)
print(data.describe())


# In[5]:


import matplotlib.pyplot as plt

# Count occurrences of each flower species
species_counts = data["species"].value_counts()

# Visualize species distribution using a bar chart
plt.bar(species_counts.index, species_counts.values)
plt.xlabel("Iris Species")
plt.ylabel("Number of Flowers")
plt.title("Distribution of Iris Flower Species")
plt.show()


# In[6]:


import seaborn as sns

# Create a pairplot to visualize relationships between all numerical features
sns.pairplot(data, hue="species")
plt.show()


# In[ ]:




