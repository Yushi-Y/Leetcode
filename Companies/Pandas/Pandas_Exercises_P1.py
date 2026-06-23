### Pandas Exercises - Data Manipulation
import pandas as pd

## Spotify - Sorting
# Get the top 10 songs
top10_songs = spotify_worldwide_daily_song_ranking[spotify_worldwide_daily_song_ranking['position'] <=10]

# Sort and output relevant fields
top10_songs.sort_values(by = ['position', 'trackname'], ascending = [False, True])[['trackname','position']].drop_duplicates()



## Airbnb - Aggregation
# Find all the neighbours
airbnb_search_details['neighbourhood'].drop_duplicates()

# Calculate the cheaptest price for each city 
airbnb_search_details.groupby(by = ['city'], as_index = False).agg({'price': 'min'})



## SalesForce - Merge
# Merge with the relevant fields from the original DataFrame
avg_sal = employee.groupby(by = ['department'], as_index = False).agg({'salary' : 'mean'}).rename(columns = {'salary' : 'average_salary'})

# Merge with the relevant fields from the original DataFrame
pd.merge(employee[['department', 'first_name', 'salary']], avg_sal, 
on = 'department', how = 'inner') # Use inner join in cases there are missing departments



## Uber - Calculate Fields
# Summarize the spends and customer acquired by channel
summ_df = uber_advertising[uber_advertising['year'].isin([2017, 2018])].groupby(
    by = ['advertising_channel'],
    as_index = False).agg({'money_spent' : 'sum', 'customers_acquired':'sum'})

# Calculate the advertising channel effectiveness        
summ_df['effct'] = summ_df['money_spent'] / summ_df['customers_acquired']

# Sort and output relevant fields
summ_df[['advertising_channel', 'effct']].sort_values(by = ['effct'])




