import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3

# For verification
print("Submitted by: 23f2001159@ds.study.iitm.ac.in")

# Load the dataset (replace with your actual file path or data source)
data = pd.read_csv("employee_performance.csv")

# Count frequency of departments
department_counts = data['Department'].value_counts()

# Frequency of "Marketing"
marketing_count = department_counts.get('Marketing', 0)
print(f"Number of employees in Marketing: {marketing_count}")

# Plot department distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Department'], discrete=True, shrink=0.8, palette='viridis')
plt.title("Distribution of Employees by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.xticks(rotation=45)

# Save interactive plot as HTML using mpld3
html_content = mpld3.fig_to_html(plt.gcf())
with open("department_distribution.html", "w") as f:
    f.write(html_content)

print("Visualization saved as department_distribution.html")
