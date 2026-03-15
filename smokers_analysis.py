import pandas as pd
import matplotlib.pyplot as plt

print("Loading dataset...")

# Load dataset from GitHub
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

print("\nFirst rows of the dataset:")
print(df.head())

# Group data by gender and smoking status
smoking_count = df.groupby(["sex", "smoker"]).size()

print("\nNumber of smokers and non-smokers by gender:")
print(smoking_count)

# Convert the result into table format for visualization
table = smoking_count.unstack()

# Create bar chart
table.plot(kind="bar")

plt.title("Smokers vs Non-Smokers by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.legend(title="Smoker")

# Save analysis result
plt.savefig("C:/Users/YOUR_USERNAME/Downloads/smoking_by_gender_analysis.png")

plt.show()

print("\nAnalysis saved as smoking_by_gender_analysis.csv")