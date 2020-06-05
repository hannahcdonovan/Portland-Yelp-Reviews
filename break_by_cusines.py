import pandas as pd

#read in cleaned_data rest file
rest_meta_data = pd.read_csv('cleaned_rest_data.csv')
del rest_meta_data['Unnamed: 0']

# for clarity's sake, renamed to id_num since this is the primary key between the reviews table 
# and the restaurant table (which contains meta data about each restaurant) -- what we will be
# merging on
rest_meta_data.rename(columns={'restaurant_id' : "id_num"}, inplace=True)

# query for all restuarants with 'Italian' categorization
italian = rest_meta_data[rest_meta_data.category.str.contains('Italian')]
print(italian)

# query for all restaurants with 'Breakfast & Brunch Categorization'
breakfast_brunch = rest_meta_data[rest_meta_data.category.str.contains('Breakfast & Brunch')]
print(breakfast_brunch)

#read in the restaurant reviews with the dates in and merge with review csv file
review_data = pd.read_csv('reviews_with_dates.csv')

# merge the tables on the id_num (primary key)
italian = pd.merge(review_data, italian, on="id_num")
breakfast_brunch = pd.merge(review_data, breakfast_brunch, on="id_num")

# now, get all the reviews!
italian = italian['review_text']
breakfast_brunch = breakfast_brunch['review_text']

# italian.to_csv('italian_reviews.csv')
# breakfast_brunch.to_csv('breakfast_brunch_reviews.csv')

all_reviews = pd.merge(review_data, rest_meta_data, on="id_num")

# del all_reviews['Unnamed: 0']

# review_data = review_data['review_text']
# review_data.to_csv('all_reviews.csv')