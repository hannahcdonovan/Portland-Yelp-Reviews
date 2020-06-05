import pandas as pd
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt

def tb_detect_polarity(text):
    return TextBlob(text).sentiment.polarity

seafood_df = pd.read_csv('../cuisine_analysis/merged_reviews_by_cuisine/seafood.csv')

# add column into dataframe with the polarity of the review
seafood_df['polarity'] = seafood_df.review_text.apply(tb_detect_polarity)

# create a subset of df with just polarities
seafood_polarities = seafood_df[['id_num', 'polarity']]

# get the average polarity of the reviews of each restaurant
sf_polarities_average = seafood_polarities.groupby(['id_num']).mean()
sf_polarities_average.rename(columns= {'polarity' : 'average_polarity'}, inplace=True)

# merge the average polarities back with the original seafood_df - now has column containing polarity of review
# and average polarity of all the reviews of the restaurant
seafood_df_with_averages = pd.merge(seafood_df, sf_polarities_average, on='id_num')

# create sub tables focused on lobsters and oysters
df_lobster = seafood_df.loc[seafood_df['review_text'].str.contains('lobster')]
df_oyster = seafood_df.loc[seafood_df['review_text'].str.contains('oyster')]

lobster_date_polarity = df_lobster[['date', 'polarity']]
oyster_date_polarity = df_oyster[['date', 'polarity']]

# see what words are collocated with lobster & oysters
for index, row in lobster_date_polarity.iterrows():
    date = row[0]
    date = date[0:7]
    lobster_date_polarity.loc[index, 'date'] = date

lobster_date_polarity = lobster_date_polarity.groupby(['date']).mean()
lobster_date_polarity = lobster_date_polarity.reset_index()
lobster_date_polarity['date'] = pd.to_datetime(lobster_date_polarity['date'],errors = 'coerce')

for index, row in oyster_date_polarity.iterrows():
    date = row[0]
    date = date[0:7]
    oyster_date_polarity.loc[index, 'date'] = date
    
oyster_date_polarity = oyster_date_polarity.groupby(['date']).mean()
oyster_date_polarity = oyster_date_polarity.reset_index()

oyster_date_polarity['date'] = pd.to_datetime(oyster_date_polarity['date'],errors = 'coerce')

oyster_date_polarity

# print(lobster_date_polarity)

ax = oyster_date_polarity.plot(x='date', y='polarity', kind='line', color='blue', figsize=(10,8))
lobster_date_polarity.plot(x='date', y='polarity', kind='line', color='red', figsize=(10,8), ax=ax)

plt.ylabel('Polarity')
plt.title('Polarity Overtime -- Lobster vs. Oyster')

plt.legend(['oyster', 'lobster'], loc='upper left')

plt.savefig('images/oyster_lobster_polarity_overtime.png')