# Hannah Donovan, Reid Brawer, Ella Weinstein
# Yelp Review Scraping

# originally ran in Jupyter notebook - would need to pip install in virtual env
import string
from lxml import html
import requests
import csv
import json
import pandas as pd

# Create an empty list called restuarants, and use Yelp Fusion API to gather names of all restuarants

# in Portland, and add to the list

# got 'raw_restaurant_data.cvs' from the Yelp Fusion API with private bearer token and requesting
# GET https://api.yelp.com/v3/businesses/search?location=Portland,ME
# JSON response body from the request was converted to csv file - mimicking relational db with
# rest_id as the primary key
data_frame = pd.read_csv('raw_rest_data.csv')

# setting up new Pandas dataframe to be converted into another CSV 
review_data_frame = pd.DataFrame(columns=('id_num', 'name', 'review_id', 'review_text', 'date'))

my_index = 0

for index, row in data_frame.iterrows():

    id_num = row[2]
    name = row[0]

    start_url = 'http://www.yelp.com/biz/%s' % id_num

    num_reviews = 180
    page_order = range(0, (num_reviews+1), 20)
    count = 0

    #going through the reviews per page
    for i in page_order:

        page = requests.get(start_url + ("?start=%s" % i))
        tree = html.fromstring(page.text)

        #case 1: if there exists informaiton in HTML tree
        if tree is not None:

            reviews = tree.xpath('//p[@itemprop="description"]/text()')
            dates = tree.xpath('//meta[@itemprop="datePublished"]/@content')

            for j, review in enumerate(reviews):

                review_data_frame.loc[my_index] = [id_num, name, my_index, review, dates[j]]

                my_index += 1



#write data frame to new csv file
review_data_frame.to_csv('reviews.csv')
