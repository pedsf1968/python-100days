import pandas as pd


df = pd.read_csv('salaries_by_college_major.csv')

# print top 5 rows
df.head()
# print number of row and columns
df.shape
# display columns attributes
df.columns
# check no number values
df.isna()
# print last 5 rows
df.tail()

# create new DataFrame without las row
clean_df = df.dropna()
clean_df.tail()
# get all values of column 'Starting Median Salary'
clean_df['Starting Median Salary']
# get max
clean_df['Starting Median Salary'].max()
# get index of max
clean_df['Starting Median Salary'].idxmax()
# Get specific value column for row 43
clean_df['Undergraduate Major'].loc[43]
clean_df['Undergraduate Major'][43]
# Gel all row 43
clean_df.loc[43]
# What college major has the highest mid-career salary? How much do graduates with this major earn?
# (Mid-career is defined as having 10+ years of experience).
clean_df.loc[clean_df['Mid-Career Median Salary'].idxmax()]
print(clean_df['Mid-Career Median Salary'].max())
print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
clean_df['Undergraduate Major'][clean_df['Mid-Career Median Salary'].idxmax()]

# Which college major has the lowest starting salary and how much do graduates earn after university?
print(clean_df['Starting Median Salary'].min())
clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]

# Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?
clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]

# A low-risk major is a degree where there is a small difference between the lowest and highest salaries. In other
# words, if the difference between the 10th percentile and the 90th percentile earnings of your major is small, then you
# can be more certain about your salary after you graduate.
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

# Lowest Risk Majors
low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()
# Majors with the Highest Potential
clean_df[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].sort_values('Mid-Career 90th Percentile Salary', ascending=False).head()
# Majors with the Greatest Spread in Salaries
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

# Count by Group
clean_df.groupby('Group').count()

# Mean by group with number formating
pd.options.display.float_format = '{:,.2f}'.format
clean_df.groupby('Group').mean()