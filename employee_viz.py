import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Email for verification: 23f2001159@ds.study.iitm.ac.in

# Create sample employee dataset
np.random.seed(42)

departments = ['Marketing', 'Sales', 'Engineering', 'HR', 'Finance', 'Operations', 'IT']
regions = ['North', 'South', 'East', 'West', 'Central']

# Generate 100 employees with realistic distribution
data = []
for i in range(100):
    employee_id = f"EMP_{i+1:03d}"
    department = np.random.choice(departments, p=[0.14, 0.18, 0.20, 0.08, 0.12, 0.15, 0.13])
    region = np.random.choice(regions)
    performance_score = np.random.normal(75, 15)
    performance_score = max(0, min(100, performance_score))  # Clamp between 0-100
    salary = np.random.normal(60000, 20000)
    salary = max(30000, salary)  # Minimum salary
    experience_years = np.random.randint(0, 20)
    
    data.append({
        'Employee_ID': employee_id,
        'Department': department,
        'Region': region,
        'Performance_Score': round(performance_score, 1),
        'Salary': round(salary, 2),
        'Experience_Years': experience_years
    })

# Create DataFrame
df = pd.DataFrame(data)

print("Employee Performance Dataset Analysis")
print("=" * 50)
print(f"Dataset shape: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())

# Calculate frequency count for Marketing department
marketing_count = df[df['Department'] == 'Marketing'].shape[0]
print(f"\nFrequency count for 'Marketing' department: {marketing_count}")

# Print department distribution
print("\nDepartment Distribution:")
dept_counts = df['Department'].value_counts()
for dept, count in dept_counts.items():
    print(f"{dept}: {count}")

# Create histogram showing distribution of departments
plt.figure(figsize=(12, 8))

# Set style for better appearance
plt.style.use('default')
sns.set_palette("husl")

# Create the histogram
plt.subplot(2, 1, 1)
dept_counts = df['Department'].value_counts()
bars = plt.bar(dept_counts.index, dept_counts.values, 
               color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57', '#FF9FF3', '#54A0FF'])
plt.title('Distribution of Employees by Department', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Department', fontsize=12)
plt.ylabel('Number of Employees', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Add value labels on bars
for bar, count in zip(bars, dept_counts.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
             str(count), ha='center', va='bottom', fontweight='bold')

# Add a second subplot for performance distribution
plt.subplot(2, 1, 2)
plt.hist(df['Performance_Score'], bins=20, color='skyblue', alpha=0.7, edgecolor='black')
plt.title('Distribution of Performance Scores', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Performance Score', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

plt.tight_layout()
plt.show()

# Additional analysis
print("\nAdditional Analysis:")
print("-" * 30)
print(f"Average Performance Score: {df['Performance_Score'].mean():.2f}")
print(f"Average Salary: ${df['Salary'].mean():,.2f}")
print(f"Average Experience: {df['Experience_Years'].mean():.1f} years")

# Regional distribution
print("\nRegional Distribution:")
region_counts = df['Region'].value_counts()
for region, count in region_counts.items():
    print(f"{region}: {count}")

# Performance by department
print("\nAverage Performance Score by Department:")
dept_performance = df.groupby('Department')['Performance_Score'].mean().sort_values(ascending=False)
for dept, score in dept_performance.items():
    print(f"{dept}: {score:.2f}")
