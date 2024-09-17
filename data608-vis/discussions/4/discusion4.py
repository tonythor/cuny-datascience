import pandas as pd
import matplotlib.pyplot as plt

# Get our data set from Kaggle here:
# https://www.kaggle.com/datasets/tonyfraser/formatted-stack-overflow-survey-2017-2022 

f = "/Users/afraser/Documents/src/krijudato/merged_stack_wide.csv"
df = pd.read_csv(f)

# Filter rows with non-null salaries
df_with_salary = df[df['AnnualSalary'].notna()]

# Specify the columns (languages) you want to analyze
language_columns = ['python', 'sql', 'java', 'javascript', 'ruby', 'scala', 'swift',  'rust', 'julia']

# Create an empty dictionary to store average salary by programming language
avg_salaries = {}

# Loop through each language column and calculate the average salary for developers who use that language
for language in language_columns:
    # Filter developers who reported using the language
    devs_using_language = df_with_salary[df_with_salary[language] == 'yes']
    
    # Calculate the average salary for those developers
    avg_salary = devs_using_language['AnnualSalary'].mean()
    
    # Store the result in the dictionary
    avg_salaries[language] = avg_salary

# Convert the dictionary to a pandas DataFrame for easy plotting/analysis
avg_salary_df = pd.DataFrame(list(avg_salaries.items()), columns=['Language', 'Avg_Salary'])

# Sort the DataFrame by Avg_Salary in descending order (highest paying on top)
avg_salary_df = avg_salary_df.sort_values(by='Avg_Salary', ascending=False)

# Applying Tufte's principles to the chart
plt.figure(figsize=(10, 6))

# Create a horizontal bar plot with simplified colors
plt.barh(avg_salary_df['Language'], avg_salary_df['Avg_Salary'], color='gray')

# Remove unnecessary chart elements (grid, borders)
plt.grid(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)

# Add title and labels with larger and bolder fonts
plt.title('Average Annual Salary of Developers by Programming Language', fontsize=16, fontweight='bold')
plt.xlabel('Average Salary (USD)', fontsize=12, fontweight='bold')
plt.ylabel('Programming Languages', fontsize=12, fontweight='bold')

# Add the attribution in the bottom right corner
plt.text(1, -0.1, 'Derived from Stack Overflow Survey data, 2017-2022', 
         fontsize=10, color='gray', ha='right', transform=plt.gca().transAxes)

# Adjust the text position to always appear within the bar or slightly outside if too short
for index, value in enumerate(avg_salary_df['Avg_Salary']):
    if value > avg_salary_df['Avg_Salary'].max() * 0.2:  # For bars with high values, place text inside
        plt.text(value - 5000, index, f'${value:,.0f}', va='center', ha='right', color='white', fontsize=10)
    else:  # For smaller values, place the text slightly outside
        plt.text(value + 5000, index, f'${value:,.0f}', va='center', ha='left', color='black', fontsize=10)

plt.tight_layout()
plt.show()