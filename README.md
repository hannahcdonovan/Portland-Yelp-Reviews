# Sentiment Analysis for Portland, Maine Restaurant Reviews
- technologies used: pandas, json, lxml (for scrapping), NLTK
- notice: for classroom assignment, needed to use csv files instead of sql db tables to use Voyant widgets
- see our results here: https://sites.google.com/view/portland-yelp-sentiment/home

Chain of Logic
- Using the Yelp Fusion API, posted a GET https://api.yelp.com/v3/businesses/search?location=Portland,ME
  request, which returned a JSON response body containing different restaurants in Portland, ME
- Converted this JSON blob into a csv file (acted as a table in the db), which had the following attributes 
  for each of the 524 restaurants returned in the response body: name, rating, restaurant_id, price, address    latitude, longitude, category 
- Using the restaurant_id from this table, we then scraped at most 100 reviews from each restaurant            
  (permitting there existed 100 reviews) -- more research would need to be done on the algorithm Yelp uses for displaying reviews on each page
- Performed numerous types of analysis based on cusine, season, date, polarity, and proximity of restaraunt to 
  water
