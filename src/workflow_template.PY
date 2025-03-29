# Standard Python Workflow for Data Analysis

# 1️⃣ Import Necessary Libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats  # For statistical inferences

# 2️⃣ Set Working Directory (Modify as Needed)
working_dir = "path/to/your/directory"
os.chdir(working_dir)  # Change directory
print(f"Working directory set to: {os.getcwd()}")

# 3️⃣ Load Dataset
file_path = "your_dataset.csv"
df = pd.read_csv(file_path)  # Load data
print("✅ Dataset Loaded Successfully")

# 4️⃣ Data Health Check
print("\n🔹 First 5 Rows:")
print(df.head())

print("\n🔹 Last 5 Rows:")
print(df.tail())

print("\n🔹 Data Dimensions (Rows, Columns):", df.shape)
print("\n🔹 Column Data Types:")
print(df.dtypes)

print("\n🔹 Missing Values:")
print(df.isnull().sum())

print("\n🔹 Summary Statistics:")
print(df.describe())

# 5️⃣ Data Cleaning (Handle Missing Values)
# Drop rows with missing values
df_cleaned = df.dropna()

# Alternatively, fill missing values with mean
df_filled = df.fillna(df.mean())

# 6️⃣ Data Subsetting & Aggregation
# Example: Subsetting specific columns
subset_df = df[["Column1", "Column2", "Column3"]]

# Example: Aggregating data
aggregated_df = df.groupby("CategoryColumn")["NumericColumn"].sum()

# 7️⃣ Statistical Inferences
# Example: Compute Pearson Correlation
corr_matrix = df.corr()
print("\n🔹 Correlation Matrix:")
print(corr_matrix)

# 8️⃣ Data Visualization
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
