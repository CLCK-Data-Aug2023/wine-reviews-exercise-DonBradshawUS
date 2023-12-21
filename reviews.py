#Import Pandas, read in CSV, and specify columns
import pandas as pd
pd.set_option('display.max_rows', 5)
df = pd.read_csv('data/winemag-data-130k-v2.csv.zip', usecols=['country', 'points'])

#Create reviews data frame
reviews = pd.DataFrame()

#Find number of unique countries
reviews['count'] = df.country.value_counts()

#Group countries with mean points
reviews['points'] = df.groupby('country').mean()

#Round points to 1 decimal
reviews.points = reviews.points.round(1)

#Print the resulting table
print(reviews)

#Send csv file to data folder
reviews.to_csv('data/reviews-per-country.csv')