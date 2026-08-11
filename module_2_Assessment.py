#import librararies
import numpy as np
import pandas as pd

df= pd.read_excel("ABC_Company.xlsx")

df.head()
#table information check

df.info()

# Peprocessing:

df["Height"] = np.random.randint(150, 181, size=len(df))
df.head()


#Analysis Tasks:

team_count = df["Team"].value_counts()

print(team_count)

team_percentage = (
    df["Team"].value_counts(normalize=True) * 100
)

print(team_percentage)

#Determine the distribution of employees across each team and calculate
# the percentage split relative to the total number of employees.

import matplotlib.pyplot as plt

# Employee count in each team
team_count = df["Team"].value_counts()

# Percentage of employees in each team
team_percentage = (team_count / len(df)) * 100

# Create bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(team_count.index, team_count.values)

# Display percentage above each bar
for bar, percentage in zip(bars, team_percentage):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{percentage:.1f}%",
        ha="center",
        va="bottom"
    )

plt.title("Distribution of Employees Across Teams")
plt.xlabel("Team")
plt.ylabel("Number of Employees")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


#Segregate employees based on their positions within the company.

position_count = df["Position"].value_counts()
print(position_count)

#Identify the predominant age group among employees.

bins = [19, 24, 29, 34, 39, 100]
labels = ["20-24", "25-29", "30-34", "35-39", "40+"]

df["Age Group"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)

age_group_count = df["Age Group"].value_counts()

print(age_group_count)

# Age Group
# 25-29    182
# 20-24    152
# 30-34     90
# 35-39     29
# 40+        3

#Histogram representation of data

import matplotlib.pyplot as plt

# Create histogram
plt.figure(figsize=(8, 5))

plt.hist(
    df["Age"],
    bins=[19, 24, 29, 34, 39, 100],
    edgecolor="black"
)

plt.title("Distribution of Employees by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Employees")

plt.xticks(
    [19, 24, 29, 34, 39, 100],
    ["19", "24", "29", "34", "39", "40+"]
)

plt.show()


# Discover which team and position have the highest salary expenditure.

team_salary = (
    df.groupby("Team")["Salary"]
      .sum()
      .sort_values(ascending=False)
)

#based on position

position_salary = (
    df.groupby("Position")["Salary"]
      .sum()
      .sort_values(ascending=False)
)


#plotimport matplotlib.pyplot as plt

# Calculate total salary by team
team_salary = (
    df.groupby("Team")["Salary"]
    .sum()
    .sort_values(ascending=False)
)

# Calculate total salary by position
position_salary = (
    df.groupby("Position")["Salary"]
    .sum()
    .sort_values(ascending=False)
)

# Create one figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 6))

# First subplot: Total salary by team
axes[0].bar(team_salary.index, team_salary.values, color="skyblue")
axes[0].set_title("Total Salary Expenditure by Team")
axes[0].set_xlabel("Team")
axes[0].set_ylabel("Total Salary")
axes[0].tick_params(axis="x", rotation=90)

# Second subplot: Total salary by position
axes[1].bar(position_salary.index, position_salary.values, color="orange")
axes[1].set_title("Total Salary Expenditure by Position")
axes[1].set_xlabel("Position")
axes[1].set_ylabel("Total Salary")

# Adjust spacing
plt.tight_layout()
plt.show()


# Finding Highest salary expenditure

print("Team with highest salary expenditure:", team_salary.idxmax())
print("Total team salary:", team_salary.max())

print("Position with highest salary expenditure:", position_salary.idxmax())
print("Total position salary:", position_salary.max())


# Result will be :

# Team with highest salary expenditure: Cleveland Cavaliers
# Total team salary: 106988689.0
# Position with highest salary expenditure: C
# Total position salary: 466377332.0


# Investigate if there's any correlation between age and salary, and
# represent it visually.

correlation = df["Age"].corr(df["Salary"])
print(correlation)


# Result will be   0.21400941226570974

# The correlation value generally ranges from -1 to +1:

# A value close to +1 indicates a strong positive correlation.
# A value close to -1 indicates a strong negative correlation.
# A value close to 0 indicates little or no linear relationship.

# Visualization: A scatter plot with a regression line is suitable for representing the relationship.


import seaborn as sns
import matplotlib.pyplot as plt

sns.regplot(data=df, x="Age", y="Salary")
plt.title("Correlation Between Age and Salary")
plt.show()

# Correlation does not prove causation. This analysis alone cannot establish that age is the cause of changes in salary.


#Graphical Representation:

# For each of the five analysis tasks above, create appropriate visualizations
# to present your findings effectively.

# 1. Team Distribution and Percentage — Bar Chart

# Employee count and percentage by team
team_count = df["Team"].value_counts()
team_percentage = (team_count / len(df)) * 100

plt.figure(figsize=(12, 6))
bars = plt.bar(team_count.index, team_count.values, color="skyblue")

# Add percentage above each bar
for bar, percentage in zip(bars, team_percentage):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{percentage:.1f}%",
        ha="center",
        va="bottom"
    )

plt.title("Distribution of Employees Across Teams")
plt.xlabel("Team")
plt.ylabel("Number of Employees")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# 2. Position Distribution — Bar Chart

# Employee count by position
position_count = df["Position"].value_counts()

plt.figure(figsize=(8, 5))
bars = plt.bar(
    position_count.index,
    position_count.values,
    color="orange"
)

# Add employee count above each bar
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        int(bar.get_height()),
        ha="center",
        va="bottom"
    )

plt.title("Distribution of Employees by Position")
plt.xlabel("Position")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()

# 3. Age-Group Distribution — Histogram

# Age-group boundaries
age_bins = [19, 24, 29, 34, 39, 100]

plt.figure(figsize=(8, 5))

plt.hist(
    df["Age"].dropna(),
    bins=age_bins,
    color="lightgreen",
    edgecolor="black"
)

plt.title("Distribution of Employees by Age Group")
plt.xlabel("Age")
plt.ylabel("Number of Employees")
plt.xticks([19, 24, 29, 34, 39, 40])
plt.tight_layout()
plt.show()

# 4. Salary Expenditure — Two Bar Charts

# Total salary expenditure by team
team_salary = (
    df.groupby("Team")["Salary"]
    .sum()
    .sort_values(ascending=False)
)

# Total salary expenditure by position
position_salary = (
    df.groupby("Position")["Salary"]
    .sum()
    .sort_values(ascending=False)
)

# Create two subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 6))

# Team salary chart
axes[0].bar(
    team_salary.index,
    team_salary.values,
    color="steelblue"
)

axes[0].set_title("Total Salary Expenditure by Team")
axes[0].set_xlabel("Team")
axes[0].set_ylabel("Total Salary")
axes[0].tick_params(axis="x", rotation=90)

# Position salary chart
axes[1].bar(
    position_salary.index,
    position_salary.values,
    color="coral"
)

axes[1].set_title("Total Salary Expenditure by Position")
axes[1].set_xlabel("Position")
axes[1].set_ylabel("Total Salary")

plt.tight_layout()
plt.show()

# 5. Age–Salary Correlation — Scatter Plot with Regression Line


# Calculate correlation
correlation = df["Age"].corr(df["Salary"])

print("Correlation between Age and Salary:", correlation)

# Scatter plot with regression line
plt.figure(figsize=(8, 5))

sns.regplot(
    data=df,
    x="Age",
    y="Salary",
    scatter_kws={"color": "blue", "alpha": 0.6},
    line_kws={"color": "red"}
)

plt.title(
    f"Correlation Between Age and Salary (r = {correlation:.2f})"
)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.tight_layout()
plt.show()



# Data Story

# Based on the dataset analysis, the "New Orleans Pelicans"  team has the highest number of employees( 16 employees), 
# representing  4.148472  % of the total workforce. The most common employee position is SG   , indicating that a larger number of employees work in this role.

# The predominant age group among employees is  25-29 (count is 182), showing that most employees fall within this age range. Regarding salary expenditure, the Cleveland Cavaliers  team has the highest total salary expenditure, while the C position accounts for the highest salary expenditure among all positions.

# The correlation coefficient between age and salary is positive correlation between age and salary (ecause the regression line slopes upward from left to right.). This indicates a weak/moderate/strong positive/negative relationship between the two variables. However, correlation does not prove causation, so this analysis alone cannot establish that age causes changes in salary.

# Overall, the analysis provides useful insights into employee distribution, workforce demographics, salary allocation, and the relationship between employee age and salary. Replace the blank spaces with the actual results obtained from your analysis.


