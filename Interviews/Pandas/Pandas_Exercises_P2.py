### Pandas Exercises - Advanced Data Manipulations

## Airbnb - Applying Functions
# Load the Airbnb dataset
df = pd.read_csv("airbnb_dataset.csv")

# Count the number of amenities for each listing
df["num_of_amenities"] = df["amenities"].apply(lambda x: len(x.split(",")))

# Group the dataset by city, sum the amenities and sort the values
city_amenities = df.groupby(by = ["city"], as_index = False).agg({'num_of_amenities': 'sum'}).sort_values(by = ['num_of_amenities'])

# Print the city with the most amenities
print("The city with the most amenities is:", city_amenities['city'][0])



## Alternative Solution - Text Manipulation
# Keep Relevant fields
rel_df = airbnb_search_details[['amenities', 'city']]

# Split the amenities string
rel_df['amenities'] = rel_df['amenities'].str.split(",")

rel_df = rel_df.explode('amenities')

# Summarize by city and print the city with the most amenities
rel_df.groupby(by = ['city'], as_index = False).agg({'amenities' : 'count'}).sort_values(by = ['amenities'], ascending = False).reset_index()['city'][0]



## City of San Francisco - Apply function for substring lookup
# Load the business dataset
df = pd.read_csv("business_dataset.csv")

# Classify buesiness names using text substring lookup
df['category'] = df['business_name'].apply(lambda x: 'restaurant' if x.lower().find('restaurant') >= 0 \
                                           else 'cafe' if x.lower().find('cafe') >= 0 or x.lower().find('coffe') >= 0 \
                                           else 'school' if x.lower().find('school') >= 0 \
                                           else 'other')

# Output relevant fields                                         
df[['business_name', 'category']].drop_duplicates()



## City of San Francisco - Pivot Table
# Pivot table to find highest payment for each employee across 2011-2014, sort rows by employee name
pd.pivot_table(data = sf_public_salaries, columns = ['year'], 
index = 'employeename', values = 'totalpay', aggfunc = 
'max', fill_value = 0).reset_index()



### Facebook - Pivot Table
# Find the first instance of different action 
summ_df = pd.pivot_table(data = facebook_web_log, index = 'user_id', columns = 
'action', aggfunc = 'min', values = 'timestamp').reset_index()[['user_id', 
'page_load', 'scroll_down']]

# Caclulate duration between page loading and first scroll down
summ_df['duration'] = summ_df['scroll_down'] - summ_df['page_load']

# Output the user details for the user with the lowest duration
summ_df.sort_values(by = ['duration'])[:1]








