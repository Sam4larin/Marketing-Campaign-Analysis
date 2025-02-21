import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Load the dataset
df = pd.read_csv('marketing_campaign_cleaned.csv', nrows=2241)

# Plot age distribution
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Plot income distribution
plt.figure(figsize=(8, 6))
sns.histplot(df['Income'], bins=30, kde=True)
plt.title('Income Distribution of Customers')
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.show()

# Count campaign responses
response_counts = df['Response'].value_counts()

# Plot response counts
plt.figure(figsize=(6, 6))
sns.barplot(x=response_counts.index, y=response_counts.values)
plt.title('Campaign Response Counts')
plt.xlabel('Response')
plt.ylabel('Count')
plt.show()

# Select relevant features for clustering
features = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds', 'Income', 'Age']

# Check for missing values
print(df[features].isnull().sum())

# Impute missing values with the median
imputer = SimpleImputer(strategy='median')
X_imputed = imputer.fit_transform(df[features])

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

# Perform KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Save the updated dataset with clusters to a new CSV file
df.to_csv('marketing_campaign_with_clusters.csv', index=False)

# Visualize clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Income', y='MntWines', hue='Cluster', data=df, palette='viridis')
plt.title('Customer Segmentation')
plt.xlabel('Income')
plt.ylabel('Spending on Wines')
plt.show()

# Group by cluster and calculate mean values
cluster_summary = df.groupby('Cluster')[features].mean()
print(cluster_summary)
