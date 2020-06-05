import pandas as pd
import nltk

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#function - creates wordcloud visualization
def create_wc(words_param, title):
    # Create and generate a word cloud image:
    wordcloud = WordCloud(background_color='white', collocations=False).generate(words_param)

    # Display the generated image:
    plt.figure(figsize=(15,15))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(title)
    plt.axis("off")
    plt.show()

#finds adjectives
def find_adjectives(reviews):
    adjective_tags = ['JJ', 'JJR', 'JJS']
    adj_list = []

    tokens = nltk.word_tokenize(reviews)
    tagged = nltk.pos_tag(tokens)

    for tag in tagged:
        if ((tag[1] in adjective_tags)) :
            adj_list.append(tag[0])

    adjs = ' '.join(adj_list)

    return adjs

#finds nouns
def find_nouns(reviews):
    noun_tags = ['NN', 'NNS']
    
    noun_list = []

    tokens = nltk.word_tokenize(reviews)
    tagged = nltk.pos_tag(tokens)

    for tag in tagged:
        if ((tag[1] in noun_tags)) :
            noun_list.append(tag[0])

    nouns = ' '.join(noun_list)

    return nouns

# get reviews table
all_reviews = pd.read_csv('../scraping_cleaning/reviews.csv')
del all_reviews['Unnamed: 0']

# get rest_meta_data table
rest_meta_data = pd.read_csv('../scraping_cleaning/cleaned_rest_data.csv')
del rest_meta_data['Unnamed: 0']
rest_meta_data.rename(columns={'restaurant_id' : "id_num"}, inplace=True)

# merge
reviews = pd.merge(all_reviews, rest_meta_data, on="id_num")
del reviews['name_y']
reviews.rename(columns={'name_x' : 'name'}, inplace=True)

# goal: create word cloud for seafood_reviews (nouns & adjectives) & all_reviews (nouns & adjectives)

#seafood merged
seafood_reviews = pd.read_csv('../cuisine_analysis/merged_reviews_by_cuisine/seafood.csv')

seafood_reviews_str = ''
for rev in seafood_reviews['review_text']:
    seafood_reviews_str += rev

#read all reviews (regardless of cuisine) into string object for tokenization and POS tagging
reviews_str = ''

for item in reviews['review_text']:
    reviews_str += item

#extract POS for seafood
seafood_adjs = find_adjectives(seafood_reviews_str)
seafood_nouns = find_nouns(seafood_reviews_str)

#extract POS for all reviews
review_adjs = find_adjectives(reviews_str)
review_nouns = find_nouns(reviews_str)

# Seafood Nouns Word Cloud
wordcloud = WordCloud(background_color='white', collocations=False).generate(seafood_nouns)

plt.figure(figsize=(15,15))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Seafood (Only Nouns)')
plt.axis("off")
plt.savefig('images/seafood_nouns_wc.png')

# Seafood Adjectives Word Cloud
wordcloud = WordCloud(background_color='white', collocations=False).generate(seafood_adjs)

plt.figure(figsize=(15,15))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Seafood (Only Adjectives)')
plt.axis("off")

plt.savefig('images/seafood_adjectives_wc.png')

# All Reviews Nouns Word Cloud
wordcloud = WordCloud(background_color='white', collocations=False).generate(review_nouns)

plt.figure(figsize=(15,15))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('All Reviews (Only Nouns)')
plt.axis("off")

plt.savefig('images/all_nouns_wc.png')

# All Reviews Adjectives Word Cloud
wordcloud = WordCloud(background_color='white', collocations=False).generate(review_adjs)

plt.figure(figsize=(15,15))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('All Reviews (Only Adjectives)')
plt.axis("off")

plt.savefig('images/all_adjectives_wc.png')