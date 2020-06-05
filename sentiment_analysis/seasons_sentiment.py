#import auxiliary modules, and then create necessary functions
import pandas as pd
from textblob import TextBlob
from datetime import date, datetime
import matplotlib.pyplot as plt

#function finds the polarity of the given review
def tb_detect_polarity(text):
    return TextBlob(text).sentiment.polarity

all_reviews = pd.read_csv('../scraping_cleaning/reviews.csv')
del all_reviews['Unnamed: 0']

rest_meta_data = pd.read_csv('../scraping_cleaning/cleaned_rest_data.csv')
rest_meta_data.rename(columns={'restaurant_id' : "id_num"}, inplace=True)

#merge the dataframes together to get all reviews
reviews = pd.merge(all_reviews, rest_meta_data, on="id_num")
del reviews['name_y']
reviews.rename(columns={'name_x' : 'name'}, inplace=True)

# seafood reviews
seafood_df = pd.read_csv('../cuisine_analysis/merged_reviews_by_cuisine/seafood.csv')
del seafood_df['Unnamed: 0']

# add polarity columns to all reviews and seafood reviews
seafood_df['polarity'] = seafood_df.review_text.apply(tb_detect_polarity)
reviews['polarity'] = reviews.review_text.apply(tb_detect_polarity)

#change the columns to be date format
seafood_df['date'] = pd.to_datetime(seafood_df['date'],errors = 'coerce')
reviews['date'] = pd.to_datetime(reviews['date'],errors = 'coerce')

seafood_df = seafood_df.rename(columns={' rating': 'rating'})

# add season column in and all reviews and seafood reviews
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]
winter = [11, 12, 1, 2]

reviews['review_season'] = ''

for index, column in reviews.iterrows():
    
    if column[3].month in spring:
        reviews.loc[index, 'review_season'] = 'spring'
    if column[3].month in summer:
        reviews.loc[index, 'review_season'] = 'summer'
    if column[3].month in fall:
        reviews.loc[index, 'review_season'] = 'fall'
    if column[3].month in winter:
        reviews.loc[index, 'review_season'] = 'winter'

# create sub frames based on season
review_summer = reviews[reviews.review_season.str.contains('summer')]
review_spring = reviews[reviews.review_season.str.contains('spring')]
review_fall = reviews[reviews.review_season.str.contains('fall')]
review_winter = reviews[reviews.review_season.str.contains('winter')]

for index, column in seafood_df.iterrows():
    
    if column[3].month in spring:
        seafood_df.loc[index, 'review_season'] = 'spring'
    if column[3].month in summer:
        seafood_df.loc[index, 'review_season'] = 'summer'
    if column[3].month in fall:
        seafood_df.loc[index, 'review_season'] = 'fall'
    if column[3].month in winter:
        seafood_df.loc[index, 'review_season'] = 'winter'

# create subframes based on season
seafood_summer = seafood_df[seafood_df.review_season.str.contains('summer')]
seafood_spring = seafood_df[seafood_df.review_season.str.contains('spring')]
seafood_fall = seafood_df[seafood_df.review_season.str.contains('fall')]
seafood_winter = seafood_df[seafood_df.review_season.str.contains('winter')]

# plots

# seafood summer
plt.figure()
seafood_summer.plot(x='polarity', y='rating', kind='scatter', color='lightgreen', figsize=(10,8))
plt.suptitle('Polarity vs. Rating (Seafood Summer Reviews)', fontsize=18)
plt.xlabel('Polarity', fontsize=16)
plt.ylabel('Rating', fontsize=16)
plt.savefig('images/polarity_rating_seafood_summer.png')

# seafood winter
plt.figure()
seafood_winter.plot(x='polarity', y='rating', kind='scatter', color='royalblue', figsize=(10,8))
plt.suptitle('Polarity vs. Rating (Seafood Winter Reviews)', fontsize=18)
plt.xlabel('Polarity', fontsize=16)
plt.ylabel('Rating', fontsize=16)
plt.savefig('images/polarity_rating_seafood_winter.png')

# all reviews summer
plt.figure()
review_summer.plot(x='polarity', y=' rating', kind='scatter', color='tomato', figsize=(10,8))
plt.suptitle('Polarity vs. Rating (All Summer Reviews)', fontsize=18)
plt.xlabel('Polarity', fontsize=16)
plt.ylabel('Rating', fontsize=16)
plt.savefig('images/polarity_rating_all_summer.png')

# all reviews winter
plt.figure()
review_winter.plot(x='polarity', y=' rating', kind='scatter', color='lightblue', figsize=(10,8))
plt.suptitle('Polarity vs. Rating (All Winter Reviews)', fontsize=18)
plt.xlabel('Polarity', fontsize=16)
plt.ylabel('Rating', fontsize=16)
plt.savefig('images/polarity_rating_all_winter.png')