# Three specific pre-processing methods used
# Handling Missing Values for Salary Column
# Standarization Salary Column
# Clean and Categorizing it

import pandas as pd
import re

# Load the dataset
file_path = "Ask A Manager Salary Survey 2021 (Responses) - Form Responses 1.csv"
df = pd.read_csv(file_path) 

# Rename columns for easier access
df.rename(columns={
    "What is your annual salary? (You'll indicate the currency in a later question. If you are part-time or hourly, please enter an annualized equivalent -- what you would earn if you worked the job 40 hours a week, 52 weeks a year.)": "Salary",
    "Job title": "Job Title",
}, inplace=True)

# Step 1: Handling Missing Values in Salary Column
df = df.dropna(subset=["Salary"])  # Remove rows where Salary is missing

# Step 2: Standardizing Salary Formats
def clean_salary(salary):
    salary = str(salary).lower().replace(',', '')  # Remove commas
    salary = re.sub(r'[^\d]', '', salary)  # Remove non-numeric characters
    return int(salary) if salary.isdigit() else None  # Convert to integer

df["Salary"] = df["Salary"].apply(clean_salary)

# Remove rows where salary couldn't be converted to a number **Updated, had some trouble with this but managed to clean it up
df = df.dropna(subset=["Salary"])

# Step 3: Cleaning and Categorizing Job Titles
def standardize_job_title(title):
    """
    Simplifies job titles by normalizing common variations.
    """
    title = str(title).strip().lower()
    if "software engineer" in title or "developer" in title:
        return "Software Engineer"
    elif "manager" in title:
        return "Manager"
    elif "director" in title:
        return "Director"
    elif "marketing" in title:
        return "Marketing Specialist"
    elif "analyst" in title:
        return "Analyst"
    elif "librarian" in title:
        return "Librarian"
    elif "accounting" in title:
        return "Accounting Professional"
    else:
        return title.title()  # Capitalize each word for readability

df["Job Title"] = df["Job Title"].apply(standardize_job_title)

# Display the cleaned dataset (first 10 rows)
print(df.head(10))

# Save cleaned data to a new CSV file
df.to_csv("cleaned_salary_data.csv", index=False)
print("Cleaned data saved as 'cleaned_salary_data.csv'")
