# clean the raw restaurant table to make the categories clear

import pandas as pd
import json

rest_data_frame = pd.read_csv('raw_rest_data.csv')

print(rest_data_frame.index)

index = 0
# string replacement to match json formatting
for category in rest_data_frame["category"]:
    category = category.replace("\'", "\"")
    rest_data_frame.at[index, 'category'] = category
    index += 1

my_index = 0
for category in rest_data_frame['category']:
    trimmed = ""
    c = json.loads(category)
    for item in c:
        title = item["title"]
        trimmed += title + ", "
    
    rest_data_frame.at[my_index, 'category'] = trimmed
    my_index += 1

print(rest_data_frame.head())

# rest_data_frame.to_csv('cleaned_rest_data.csv')