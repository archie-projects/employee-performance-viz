import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# -------------------------
# 1. Load the dataset
# -------------------------
# You can replace this with your actual dataset file
data = {
    "EmployeeID": range(1, 21),
    "Name": ["Emp" + str(i) for i in range(1, 21)],
    "Department": [
        "Marketing", "Sales", "HR", "IT", "Finance",
        "Marketing", "IT", "Sales", "HR", "Finance",
        "Marketing", "Sales", "Finance", "HR", "IT",
        "Marketing", "Finance", "Sales", "HR", "IT"
    ],
    "Region": [
        "North", "South", "East", "West", "North",
        "South", "East", "West", "North", "South",
        "East", "West", "North", "South", "East",
        "West", "North", "South", "East", "West"
    ],
    "PerformanceScore": [85, 77, 90, 70, 88, 92, 66, 73, 95, 81,
                         78, 84, 89, 91, 76, 82, 87, 93, 79, 80]
}

df = pd.DataFrame(data)

# -------------------------
# 2. Frequency count of Marketing department
# -------------------------
marketing_count = (df["Department"] == "Marketing").sum()
print("Frequency count of Marketing department:", marketing_count)

# -------------------------
# 3. Plot histogram of department distribution
# -------------------------
plt.figure(figsize=(8, 6))
df["Department"].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Distribution of Employees by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()

# -------------------------
# 4. Save plot as interactive HTML
# -------------------------
html_str = mpld3.fig_to_html(plt.gcf())
with open("employee_department_distribution.html", "w") as f:
    f.write(html_str)

print("Visualization saved as employee_department_distribution.html")

# Verification email
print("Verification Email: 23f2001159@ds.study.iitm.ac.in")
