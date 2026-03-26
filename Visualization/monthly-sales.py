import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("monthly-sales.csv")

print("\n========== COMPANY SALES ANALYSIS ==========\n")

# Preview Dataset
print("Dataset Preview:")
print(df.to_string(index=False)) 

# Sales Summary
print("\n========== SALES SUMMARY ==========\n")

print("Total Annual Sales:", df["Sales"].sum())
print("Average Monthly Sales:", round(df["Sales"].mean(), 2))
print("Highest Sales:", df["Sales"].max())
print("Lowest Sales:", df["Sales"].min())

# Best & Worst Months
best_month = df.loc[df["Sales"].idxmax()]
worst_month = df.loc[df["Sales"].idxmin()]

print("\n========== BEST MONTH ==========\n")
print(f"Month: {best_month['Month']}")
print(f"Sales: {best_month['Sales']}")

print("\n========== WORST MONTH ==========\n")
print(f"Month: {worst_month['Month']}")
print(f"Sales: {worst_month['Sales']}")

# Monthly Growth
df["MoM-Growth%"] = df["Sales"].pct_change() * 100

print("\n========== MONTH-OVER-MONTH GROWTH (%) ==========\n")
print(df[["Month", "Sales", "MoM-Growth%"]].to_string(index=False))

# Graphs
# 1.Line Chart: Sales Trend Graph
plt.figure(figsize=(10,5))  

plt.plot(df["Month"], df["Sales"], marker='o', linewidth=2, color='lightblue')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.xticks(df["Month"])  
plt.grid(True)
plt.tight_layout()  
plt.show()

# 2.Line Chart: Highlight Best & Worst Month
plt.figure(figsize=(10,5))

plt.plot(df["Month"], df["Sales"], marker='o', linewidth=2, color='lightblue')
plt.scatter(best_month["Month"], best_month["Sales"], color='green', s=100, label="Best Month")
plt.scatter(worst_month["Month"], worst_month["Sales"], color='red', s=100, label="Worst Month")

plt.title("Sales Trend with Highlights")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.xticks(df["Month"])
plt.legend() 
plt.grid(True)
plt.tight_layout()
plt.show()

# 3.Bar Chart: Sales Distribution
plt.figure(figsize=(10,5))

avg_sales = df["Sales"].mean()
colors = ['green' if val >= avg_sales else 'red' for val in df["Sales"]]

plt.bar(df["Month"], df["Sales"], color=colors)
plt.title("Monthly Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.xticks(df["Month"])
plt.grid(axis='y')
plt.tight_layout()
plt.show()