import pandas as pd

#read in cleaned_data rest file
rest_meta_data = pd.read_csv('cleaned_rest_data.csv')

del rest_meta_data['Unnamed: 0']

rest_meta_data.head()

#alter current dataframe to contain only the restaurants that have category "Italina" -- does not contain reviews
italian = rest_meta_data[rest_meta_data.category.str.contains('Italian')]

#alter current dataframe to contain only "breakfast and brunch" categories
breakfast_brunch = rest_meta_data[rest_meta_data.category.str.contains('Breakfast & Brunch')]

italian.rename(columns={'restaurant_id' : "id_num"}, inplace=True)
breakfast_brunch.rename(columns={'restaurant_id' : "id_num"}, inplace=True)

#read in the restaurant reviews with the dates in and merge with review csv file

review_data = pd.read_csv('reviews_with_dates.csv')

italian = pd.merge(review_data, italian, on="id_num")
breakfast_brunch = pd.merge(review_data, breakfast_brunch, on="id_num")

italian = italian['review_text']
breakfast_brunch = breakfast_brunch['review_text']

italian.to_csv('italian_reviews')
breakfast_brunch.to_csv('breakfast_brunch_reviews')

rest_meta_data.rename(columns={'restaurant_id' : "id_num"}, inplace=True)

all_reviews = pd.merge(review_data, rest_meta_data, on="id_num")

del all_reviews['Unnamed: 0']

# all_reviews

review_data = review_data['review_text']
review_data.to_csv('all_reviews.csv')