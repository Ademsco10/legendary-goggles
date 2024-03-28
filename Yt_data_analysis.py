import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df = pd.read_csv(r"C:\Users\adems\Downloads\youtubers_df.csv")
# Display the first few rows of the DataFrame
df.head()
#Check the structure of the DataFrame
df.info()
# Summary statistics of numerical variables
df.describe()
# Check for missing data
df.isnull().sum()
# Check for outliers using box plots
numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
for col in numerical_cols:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df[col])
    plt.title(col)
    plt.show()
# Count occurrences of each category
category_counts = df['Categories'].value_counts()

# Display the top categories
top_categories = category_counts.head(10)
print("Top Categories:")
print(top_categories)

# Calculate correlation coefficients
corr_likes = df['Suscribers'].corr(df['Likes'])
corr_comments = df['Suscribers'].corr(df['Comments'])

print("Correlation Coefficient between Subscribers and Likes:", corr_likes)
print("Correlation Coefficient between Subscribers and Comments:", corr_comments)

# Distribution of streamers by country
country_distribution = df['Country'].value_counts()

# Display the top countries
top_countries = country_distribution.head(10)
print("Top Countries of Streamers:")
print(top_countries)

# Determine if there are regional preferences for specific content categories
category_country = df.groupby(['Categories', 'Country']).size().unstack().fillna(0)
print("Category Distribution by Country:")
print(category_country)

# Calculate average metrics
average_metrics = df[['Suscribers', 'Likes', 'Visits', 'Comments']].mean()

# Visualize average metrics
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
average_metrics.plot(kind='bar', color=['blue', 'green', 'orange', 'red'])
plt.title('Average Metrics Among Top Streamers')
plt.xlabel('Metrics')
plt.ylabel('Average Value')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
# Explore distribution of content categories
category_distribution = df['Categories'].value_counts()

# Display categories with the highest number of streamers
print("Categories with the Highest Number of Streamers:")
print(category_distribution.head(10))

# Group by category and calculate average metrics
category_avg_metrics = df.groupby('Categories')[['Suscribers', 'Likes', 'Visits', 'Comments']].mean()

# Identify categories with exceptional performance metrics
exceptional_categories = category_avg_metrics[(category_avg_metrics > category_avg_metrics.mean()).all(axis=1)]
print("Categories with Exceptional Performance Metrics:")
print(exceptional_categories)
# Calculate average performance metrics
average_performance = df[['Suscribers', 'Likes', 'Visits', 'Comments']].mean()

# Identify streamers with above-average performance
above_average_streamers = df[(df['Suscribers'] > average_performance['Suscribers']) &
                             (df['Likes'] > average_performance['Likes']) &
                             (df['Visits'] > average_performance['Visits']) &
                             (df['Comments'] > average_performance['Comments'])]

print("Streamers with Above Average Performance Metrics:")
print(above_average_streamers)

# Identify top-performing content creators based on subscribers
top_performing_creators = df.nlargest(10, 'Suscribers')
print("Top Performing Content Creators:")
print(top_performing_creators)

