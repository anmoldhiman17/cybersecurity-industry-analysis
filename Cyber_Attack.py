import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from zip (no change here)
df = pd.read_csv("Chapter 2/Internship Project 2 Gncipl/archive (6).zip")

# Confirm columns
print("📋 Columns:", df.columns.tolist())

# Clean: Drop missing rows in required columns
df.dropna(subset=['Target Industry', 'Attack Type', 'Year'], inplace=True)

# 🔹 Top 10 Target Industries
plt.figure(figsize=(10, 6))
sns.countplot(y='Target Industry', data=df, order=df['Target Industry'].value_counts().index[:10])
plt.title("Top 10 Targeted Industries in Cyber Attacks")
plt.xlabel("Number of Attacks")
plt.ylabel("Industry")
plt.tight_layout()
plt.show()

# 🔹 Attack Count Per Year
plt.figure(figsize=(10, 6))
sns.countplot(x='Year', data=df, order=sorted(df['Year'].dropna().unique()))
plt.title("Cyber Attacks Per Year")
plt.xlabel("Year")
plt.ylabel("Attack Count")
plt.tight_layout()
plt.show()

# 🔹 Year-wise Attack Trends for Top 5 Industries
industry_trend = df.groupby(['Year', 'Target Industry']).size().unstack().fillna(0)
top_industries = df['Target Industry'].value_counts().index[:5]

plt.figure(figsize=(12, 6))
industry_trend[top_industries].plot()
plt.title("Cyber Attacks in Top 5 Industries Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Attacks")
plt.grid(True)
plt.tight_layout()
plt.show()

# 🔹 Pie Chart for Attack Types
plt.figure(figsize=(6, 6))
df['Attack Type'].value_counts().head(6).plot.pie(autopct='%1.1f%%', startangle=140)
plt.title("Top Attack Types")
plt.ylabel("")
plt.show()

# 🔹 Heatmap: Target Industry vs Attack Type
pivot = pd.crosstab(df['Target Industry'], df['Attack Type'])
plt.figure(figsize=(14, 10))
sns.heatmap(pivot, cmap='YlGnBu', linewidths=0.5)
plt.title("Industry vs Attack Type Heatmap")
plt.xlabel("Attack Type")
plt.ylabel("Target Industry")
plt.tight_layout()
plt.show()
