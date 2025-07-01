import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("C:\\Users\\Yashika malik\\Downloads\\world_population.csv")
print(df)

sns.set(style="whitegrid")
plt.style.use("ggplot")

# Display the first 5 rows
print(df.head())

# Display the last 5 rows
print(df.tail())

# Step 3: Dataset overview
print("Shape of dataset:", df.shape)
print(df.info())

# Step 4: Basic statistics of numerical columns
print(df.describe())
print("Original Columns:", df.columns)
df.columns = df.columns.str.strip()

# Data cleaning
print(df.isnull().sum())
print(df.dropna())
df['2022 Population'] = pd.to_numeric(df['2022 Population'], errors='coerce')
df = df.dropna(subset=['2022 Population'])

# Sort the dataset for bar chart
df_sorted = df.sort_values(by='2022 Population', ascending=False)
top10 = df_sorted.head(10)

# Bar chart 
plt.figure(figsize=(10, 6))
colors = plt.cm.viridis(np.linspace(0, 1, len(top10)))  
plt.bar(top10['Country/Territory'], top10['2022 Population'], color=colors)
plt.title('Top 10 Most Populous Countries in 2022')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


'''# Plot histogram + KDE
plt.figure(figsize=(10, 6))
sns.histplot(df['2022 Population'], bins=30, kde=True, color="green")
plt.title("Population Distribution Across Countries 2022", fontsize=14)
plt.xlabel("Population", fontsize=12)
plt.ylabel("Number of Countries", fontsize=12)
plt.tight_layout()
plt.show()

#India's Population Distribution in 2022
india_data = df[df['Country/Territory'].str.strip().str.lower() == 'india']
total_population = float(india_data['2022 Population'].iloc[0])
age_groups = {
    '0–20 Years': 0.35,
    '21–64 Years': 0.55,
    '65+ Years': 0.10
}
group_populations = [round(total_population * pct / 1e6) for pct in age_groups.values()]
colors = ['dodgerblue', 'deeppink', 'red']

# Plot
plt.figure(figsize=(10, 6))
bars = plt.bar(age_groups.keys(), group_populations, color=colors)

# Add labels on top
for bar, value in zip(bars, group_populations):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
             f'{int(value)} Mn', ha='center', fontsize=12, weight='bold')

plt.title("India's Population Distribution in 2022", fontsize=14)
plt.xlabel("Age Group", fontsize=12)
plt.ylabel("Population (in Millions)", fontsize=12)
plt.tight_layout()
plt.show()'''
