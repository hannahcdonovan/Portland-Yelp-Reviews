import pandas as pd

# read in reviews (which have primary_key id_num) to pandas dataframe
all_reviews = pd.read_csv('../scraping_cleaning/reviews.csv')
del all_reviews['Unnamed: 0']

# read in restaurant meta data (which has primary_key id_num) to pandas dataframe
rest_meta_data = pd.read_csv('../scraping_cleaning/cleaned_rest_data.csv')
del rest_meta_data['Unnamed: 0']
rest_meta_data.rename(columns={'restaurant_id' : "id_num"}, inplace=True)

# merge the two tables together on primary key
reviews = pd.merge(all_reviews, rest_meta_data, on="id_num")
del reviews['name_y']
reviews.rename(columns={'name_x' : 'name'}, inplace=True)

#break into subframes by cuisine
italian = reviews[reviews.category.str.contains('Italian')]
breakfast_brunch = reviews[reviews.category.str.contains('Breakfast & Brunch')]
burgers = reviews[reviews.category.str.contains('Burgers')]
american = reviews[reviews.category.str.contains('American')]
seafood = reviews[reviews.category.str.contains('Seafood')]

# write merged tables
# italian.to_csv('merged_reviews_by_cuisine/italian.csv')
# breakfast_brunch.to_csv('merged_reviews_by_cuisine/breakfast_brunch.csv')
# burgers.to_csv('merged_reviews_by_cuisine/burgers.csv')
# american.to_csv('merged_reviews_by_cuisine/american.csv')
# seafood.to_csv('merged_reviews_by_cuisine/seafood.csv')

#subdivide cuisines to just get reviews text of each cuisine - just reviews
italian_reviews = italian['review_text']
breakfast_brunch_reviews = breakfast_brunch['review_text']
burgers_reviews = burgers['review_text']
american_reviews = american['review_text']
seafood_reviews = seafood['review_text']
all_rev = reviews['review_text']

# write the above to own csv file - commented out becuase already done
# italian_reviews.to_csv('reviews_by_cuisine/italian_reviews.csv')
# breakfast_brunch_reviews.to_csv('reviews_by_cuisine/breakfast_brunch_reviews.csv')
# burgers_reviews.to_csv('reviews_by_cuisine/burgers_reviews.csv')
# american_reviews.to_csv('reviews_by_cuisine/american_reviews.csv')
# seafood_reviews.to_csv('reviews_by_cuisine/seafood_reviews.csv')